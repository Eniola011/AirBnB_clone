#!/usr/bin/python3
"""Unittest for Amenity Module"""


import unittest
from models.amenity import Amenity
import datetime


class TestState(unittest.TestCase):
    """ Tests Amenity Subclass """

    amen = Amenity()

    def testClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.amen)), "<class 'models.amenity.Amenity'>")

    def testAmenityInheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amen, Amenity)

    def testHasAttr(self):
        """test for user class attributes"""
        self.assertTrue(hasattr(self.amen, 'name'))
        self.assertTrue(hasattr(self.amen, 'id'))
        self.assertTrue(hasattr(self.amen, 'created_at'))
        self.assertTrue(hasattr(self.amen, 'updated_at'))

    def test_types(self):
        """test the type of attribute in user subclass"""
        self.assertIsInstance(self.amen.name, str)
        self.assertIsInstance(self.amen.id, str)
        self.assertIsInstance(self.amen.created_at, datetime.datetime)
        self.assertIsInstance(self.amen.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
