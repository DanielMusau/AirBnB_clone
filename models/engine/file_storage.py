#!/usr/bin/env python3
"""Module contains class that serializes instance to a JSON
file and deserializes JSON file to instances.
"""
import json
import os


class FileStorage:
    """Class that serializes instances to a JSON file and
    deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file."""
        dict_obj = {}

        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(dict_obj, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'."""
        from models.base_model import BaseModel
        from models.user import User

        dict_obj = {'BaseModel': BaseModel, 'User': User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                for key, value in json.load(f).items():
                    self.new(dict_obj[value['__class__']](**value))
