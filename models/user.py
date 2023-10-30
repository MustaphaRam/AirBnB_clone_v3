#!/usr/bin/python3
"""This is the user module or class"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from hashlib import md5
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    if storage_type == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all, delete, delete-orphan',
                            backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                            backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """
        initialize User Model, inherits from BaseModel
        """
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """
        getter for password
        :return: password (hashed)
        """
        return self.__dict__.get("password")
    
    @password.setter
    def password(self, password):
        """
        Password setter, with md5 hasing
        :param password: password
        :return: nothing
        """
        self.__dict__["password"] = md5(password.encode('utf-8')).hexdigest()
