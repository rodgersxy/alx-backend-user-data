#!/usr/bin/env python3
"""
Implement a hash_password function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function called hash_password
    args:
        password: string password
    return: bytes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function called is_valid
    args:
        hashed_password: bytes
        password: string
    return: bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
