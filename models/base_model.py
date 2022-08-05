#!/usr/bin/python3
"""
    Base Module For AIRBNB_CLONE
"""

from datetime import datetime as dt
import models
import uuid


class BaseModel():
    """
    Base Model

    Attributes:
        id: (string) assign with a uuid
        created_at: (datetime) assign with current datetime
        updated_at: (datetime) assign with current datetime
    """
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ Base Model Constructor: use kwargs to create new instances """
        if kwargs:
            for attr_name, attr_value in kwargs.items():
                if attr_name == "created_at" or attr_name == "updated_at":
                    # Format created_at and updated_at before creating instance
                    attr_value = dt.strptime(attr_value, self.format)
                elif attr_name == "__class__":
                    continue

                setattr(self, attr_name, attr_value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """ Prints [<class name>] (<self.id>) <self.__dict__> """
        value = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return value

    def save(self):
        """
            Updates public instance attribute updated_at
            with current datetime
        """
        self.updated_at = dt.now()
        models.storage.save()

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
