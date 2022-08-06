#!/usr/bin/python3
"""" Place Module For AirBnB Clone """

from models import amenity
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class

    Public Instance Attribute:
        city_id (string)
        user_id (string)
        name (string)
        description (string)
        number_rooms (integer)
        number_bathrooms (integer)
        max_guest (integer)
        price_by_night (integer)
        latitude (float)
        longitude (float)
        amenity_ids (list of amentiy_id)

    Attributes from BaseModel:
        id (string: uuid)
        created_at (datetime)
        updated_at (datetime)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    longitude = 0
    latitude = 0
    amenity_ids = []
