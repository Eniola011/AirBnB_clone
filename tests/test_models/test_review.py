#!/usr/bin/python3
"""Unittest for Review Module"""


import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Tests Review Subclass """

    rvw = Review()

    def testSubClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.rvw)),
                         "<class 'models.review.Review'>")

    def testReviewInheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.rvw, Review)

    def testHasAttr(self):
        """test for review class attributes"""
        self.assertTrue(hasattr(self.rvw, 'place_id'))
        self.assertTrue(hasattr(self.rvw, 'id'))
        self.assertTrue(hasattr(self.rvw, 'created_at'))
        self.assertTrue(hasattr(self.rvw, 'updated_at'))
        self.assertTrue(hasattr(self.rvw, 'user_id'))
        self.assertTrue(hasattr(self.rvw, 'text'))

    def testIsinstance(self):
        """test the type of attribute in review subclass"""
        self.assertIsInstance(self.rvw.place_id, str)
        self.assertIsInstance(self.rvw.id, str)
        self.assertIsInstance(self.rvw.created_at, datetime.datetime)
        self.assertIsInstance(self.rvw.updated_at, datetime.datetime)
        self.assertIsInstance(self.rvw.text, str)
        self.assertIsInstance(self.rvw.user_id, str)


if __name__ == '__main__':
    unittest.main()
