#!/usr/bin/python3
"""" Review Module For AirBnB Clone """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class

    Public Instance Attribute:
        place_id (string)
        user_id (string)
        text (string)

    Attributes from BaseModel:
        id (string: uuid)
        created_at (datetime)
        updated_at (datetime)
    """

    place_id = ""
    user_id = ""
    text = ""
