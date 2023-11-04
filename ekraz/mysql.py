#!/usr/bin/env python3
"""
"""
# install library
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

# python standard library
from datetime import timezone, datetime

# python standard library
from uuid import uuid4

Base = DeclarativeBase()

class Base(DeclarativeBase):

    """
    Base
    ====
    Base of all model

    Args
    ====
    + id: primary key
    + create_at: creation date
    + update_at: modification date
    """

    id: Mapped[str] = mapped_column(String, primary_key=True, default=str(uuid4()))
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=timezone))
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=timezone), onupdate=datetime.now(tz=timezone))


profil_db = SQLAlchemy(model_class=Base)
auth_db = SQLAlchemy(model_class=Base)
