#!/usr/bin/python3
"""" City Module For AirBnB Clone """

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class

    Public Instance Attribute:
        state_id (string)
        name (string)

    Attributes from BaseModel:
        id (string: uuid)
        created_at (datetime)
        updated_at (datetime)
    """

    state_id = ""
    name = ""
