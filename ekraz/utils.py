#!/usr/bin/env python3
"""
"""
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.hash import bcrypt



def encrypt(password: str) -> str:
    return generate_password_hash(password=password, method=bcrypt.using(rounds=12))


def decrypt(password: str, new_password: str):
    return check_password_hash(password, new_password)
