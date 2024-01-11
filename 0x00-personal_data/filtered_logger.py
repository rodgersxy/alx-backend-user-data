#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List
import logging
from mysql.connector import connection
from os import environ

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        function called filter_datum that returns the log message obfuscated
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated
    args:
        fields: list of fields to obfuscate
        redaction: string to redact
        message: log line
        separator: character separating field and value
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    function called get_logger that returns a logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """
    function called get_db that returns a connection to the database
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    connector = connection.MySQLConnection(
        user=username, password=password, host=db_host, database=db_name
    )
    return connector
