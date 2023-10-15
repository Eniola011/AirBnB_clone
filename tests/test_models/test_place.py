#!/usr/bin/python3
"""Unittest for Place Module"""


import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """ Tests Place Subclass """

    playce = Place()

    def testSubClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.playce)),
                         "<class 'models.place.Place'>")

    def testPlaceInheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.playce, Place)

    def testHasAttr(self):
        """test for user class attributes"""
        self.assertTrue(hasattr(self.playce, 'name'))
        self.assertTrue(hasattr(self.playce, 'id'))
        self.assertTrue(hasattr(self.playce, 'created_at'))
        self.assertTrue(hasattr(self.playce, 'updated_at'))
        self.assertTrue(hasattr(self.playce, 'city_id'))
        self.assertTrue(hasattr(self.playce, 'user_id'))
        self.assertTrue(hasattr(self.playce, 'name'))
        self.assertTrue(hasattr(self.playce, 'description'))
        self.assertTrue(hasattr(self.playce, 'number_rooms'))
        self.assertTrue(hasattr(self.playce, 'number_bathrooms'))
        self.assertTrue(hasattr(self.playce, 'max_guest'))
        self.assertTrue(hasattr(self.playce, 'price_by_night'))
        self.assertTrue(hasattr(self.playce, 'latitude'))
        self.assertTrue(hasattr(self.playce, 'longitude'))
        self.assertTrue(hasattr(self.playce, 'amenity_ids'))

    def test_types(self):
        """test the type of attribute in place subclass"""
        self.assertIsInstance(self.playce.name, str)
        self.assertIsInstance(self.playce.id, str)
        self.assertIsInstance(self.playce.created_at, datetime.datetime)
        self.assertIsInstance(self.playce.updated_at, datetime.datetime)
        self.assertIsInstance(self.playce.city_id, str)
        self.assertIsInstance(self.playce.user_id, str)
        self.assertIsInstance(self.playce.description, str)
        self.assertIsInstance(self.playce.number_rooms, int)
        self.assertIsInstance(self.playce.number_bathrooms, int)
        self.assertIsInstance(self.playce.max_guest, int)
        self.assertIsInstance(self.playce.price_by_night, int)
        self.assertIsInstance(self.playce.latitude, float)
        self.assertIsInstance(self.playce.longitude, float)
        self.assertIsInstance(self.playce.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
