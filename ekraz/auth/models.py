#!/usr/bin/env python3
"""
"""
# install library
from sqlalchemy import Integer, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

# standard library
from datetime import datetime, timezone

# project module
from ..mysql import auth_db as db



# user authentication

class Auth(db.Model):

    __bind_key__ = "auth"

    pseudo: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def to_dict(self):

        return {
            'pseudo': self.pseudo,
        }