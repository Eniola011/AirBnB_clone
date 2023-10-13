#!/usr/bin/python3
"""Parent Class: Base Model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Parent Class to Inherit From"""

    def __init__(self, *arg, **kwargs):
        """Initialization of BaseModel"""
        if kwargs and kwargs is not None:
            for key in kwargs:
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.\
                        strptime(kwargs["created_at"], time_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.\
                        strptime(kwargs["updated_at"], time_format)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints representation of a class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

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
        class_name = self.__class__.__name__
        dicty = self.__dict__.copy()
        dicty['__class__'] = class_name
        dicty['created_at'] = self.created_at.isoformat()
        dicty['updated_at'] = self.updated_at.isoformat()
        return dicty
