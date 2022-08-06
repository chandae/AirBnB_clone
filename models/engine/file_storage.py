#!/usr/bin/python3
"""
    File Storage Module - File Serializer and File Deserializer
"""

import json
from models.base_model import BaseModel
from models.user import User
import os.path


class FileStorage():
    """
        Serializes instances to a JSON file
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __object """
        return self.__objects

    def new(self, obj):
        """ Add new object <obj> to __objects """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        instance_dict = {}
        for key, value in self.__objects.items():
            instance_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='UTF-8') as json_file:
            json.dump(instance_dict, json_file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects if file exists
        if file does not exist: do nothing
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as json_file:
                instance_dict = json.load(json_file)

            my_objects = {}
            for key, value in instance_dict.items():
                class_name = value['__class__']
                my_objects[key] = eval(class_name)(**value)
            self.__objects.update(my_objects)
