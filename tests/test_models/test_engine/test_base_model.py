#!/usr/bin/python3
"""Unittest for BaseModel"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the class BaseModel"""

    def setUp(self):
        """sets up basemodel"""
        self.baseModel = BaseModel()

    def testAttribute(self):
        """test the attribute of basemodel"""
        self.assertTrue(hasattr(self.baseModel, "created_at"))
        self.assertFalse(hasattr(self.baseModel, "updated_at"))
        self.assertEqual(self.baseModel.__class__.__name__, "BaseModel")

    def testSave(self):
        """test save method in base class"""
        self.testModel.save()
        self.assertTrue(hasattr(self.baseModel, "updated_at"))

#def testStrng(self):
        """test str method"""
