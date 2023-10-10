#!/usr/bin/python3
"""
Parent Class: Base Model
"""
from datetime import datetime
import uuid


class BaseModel():
    """ Parent Class to Inherit From """

    def __init__(self, *arg, **kwargs):
        """ Initialization of BaseModel """
        if not kwargs:
            self.id = str(uuid.uuid(4))
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ Prints representation of a class """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

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
