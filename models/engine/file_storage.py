#!/usr/bin/python3
"""FileStorage"""


import json
import os


class FileStorage():
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            dicty = {kii: value.to_dict() for kii,
                     value in FileStorage.__objects.items()}
            json.dump(dicty, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User

        dicty = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                for key, value in json.load(fd).items():
                    self.new(dicty[value["__class__"]](**value))
