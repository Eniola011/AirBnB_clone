#!/usr/bin/python3
"""Unittest for BaseModel"""


import unittest
import datetime
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test the class BaseModel"""
    my_model = BaseModel()

    def testBasemodel(self):
        """Test attributes in Base Model"""
        self.my_model = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual(self.my_model.id, my_model_json['id'])
        self.assertEqual(self.my_model.name, my_model_json['name'])

    def testSave(self):
        """test save method in base class"""
        self.my_model.first_name = "First"
        self.my_model.save()
        dict1 = self.my_model.to_dict()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        self.my_model.first_name = "Second"
        self.my_model.save()
        dict2 = self.my_model.to_dict()
        self.assertEqual(dict1['created_at'], dict2['created_at'])
        self.assertNotEqual(dict1['updated_at'], dict2['updated_at'])


if __name__ == '__main__':
    unittest.main()
