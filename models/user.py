#!/usr/bin/python3
""" User Module For AirBnB Clone """


from models.base_model import BaseModel


class User(BaseModel):
    """
        User Class

        Public Class Attributes:
            email (string)
            password (string)
            first_name (string)
            last_name (string)
    """

    email = ""
    password = ""
    last_name = ""
    first_name = ""
