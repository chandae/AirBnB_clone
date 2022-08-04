#!/usr/bin/python3
"""
    Base Module For AIRBNB_CLONE
"""

from datetime import datetime
import uuid


class BaseModel():
    """
    Base Model
    Attributes:
        id: (string) assign with a uuid
        created_at: (datetime) assign with current datetime
        updated_at: (datetime) assign with current datetime
    """

    def __init__(self):
        """ Base Model Constructor """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """ Prints [<class name>] (<self.id>) <self.__dict__> """
        print(f"[{self.__class__.__name__}]", f"({self.id})", self.__dict__)
        return ""

    def save(self):
        """
            Updates public instance attribute updated_at
            with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing all
            keys/values of __dicit__ of the instance
            Also contains key: __class__ with value == instance class
        """
        instance_dict = {"__class__": self.__class__.__name__, **self.__dict__}

        # Convert created_at and updated_at to format: %Y-%m-%dT%H:%M:%S.%f
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        instance_dict["id"] = str(instance_dict["id"])
        return instance_dict
