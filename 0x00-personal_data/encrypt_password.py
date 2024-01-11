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
