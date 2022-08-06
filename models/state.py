#!/usr/bin/python3
"""" State Module For AirBnB Clone """

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class

    Public Instance Attribute:
        name (string)

    Attributes from BaseModel:
        id (string: uuid)
        created_at (datetime)
        updated_at (datetime)
    """

    name = ""
