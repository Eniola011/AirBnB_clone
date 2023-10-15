#!/usr/bin/python3
"""Unittest for City Module"""


import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ Tests City Subclass """

    sity = City()

    def testSubClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.sity)),
                         "<class 'models.city.City'>")

    def testCityInheritance(self):
        """test if City is a subclass of BaseModel"""
        self.assertIsInstance(self.sity, City)

    def testHasAttr(self):
        """test for city class attributes"""
        self.assertTrue(hasattr(self.sity, 'state_id'))
        self.assertTrue(hasattr(self.sity, 'id'))
        self.assertTrue(hasattr(self.sity, 'created_at'))
        self.assertTrue(hasattr(self.sity, 'updated_at'))
        self.assertTrue(hasattr(self.sity, 'name'))

    def testIsinstance(self):
        """test the type of attribute in city subclass"""
        self.assertIsInstance(self.sity.state_id, str)
        self.assertIsInstance(self.sity.id, str)
        self.assertIsInstance(self.sity.created_at, datetime.datetime)
        self.assertIsInstance(self.sity.updated_at, datetime.datetime)
        self.assertIsInstance(self.sity.name, str)


if __name__ == '__main__':
    unittest.main()
