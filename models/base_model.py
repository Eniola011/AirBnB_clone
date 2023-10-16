#!/usr/bin/python3
"""Parent Class: Base Model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Parent Class to Inherit From"""

    def __init__(self, *arg, **kwargs):
        """Initialization of BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], time_format)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Prints representation of a class"""
        className = "[" + self.__class__.__name__ + "]"
        dic = {ke: val for (ke, val) in self.__dict__.items()
               if (not val) is False}
        return className + " (" + self.id + ") " + str(dic)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dicList = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dicList[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not value:
                    pass
                else:
                    dicList[key] = value
        dicList['__class__'] = self.__class__.__name__

        return dicList
