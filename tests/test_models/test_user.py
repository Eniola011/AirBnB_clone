#!/usr/bin/python3
"""Unittest User Class"""


from models import storage
from models.base_model import BaseModel
from models.user import User
import datetime
import unittest


class TestUser(unittest.TestCase):
    """Tests for User Class"""
    usr = User()

    def testClass(self):
        """test for existence of class"""
        self.assertEqual(str(type(self.usr)), "<class 'models.user.User'>")

    def testClassInheritance(self):
        """tests whether user class is a subclass of BaseModel super class"""
        self.assertIsInstance(self.usr, User)

    def testHasAttr(self):
        """test for user class attributes"""
        self.assertTrue(hasattr(self.usr, 'email'))
        self.assertTrue(hasattr(self.usr, 'password'))
        self.assertTrue(hasattr(self.usr, 'first_name'))
        self.assertTrue(hasattr(self.usr, 'last_name'))
        self.assertTrue(hasattr(self.usr, 'id'))
        self.assertTrue(hasattr(self.usr, 'created_at'))
        self.assertTrue(hasattr(self.usr, 'updated_at'))

    def testtype(self):
        """test the type of attribute in user subclass"""
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.id, str)
        self.assertIsInstance(self.usr.created_at, datetime.datetime)
        self.assertIsInstance(self.usr.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
