#!/usr/bin/python3
"""Unittest for State Module"""


import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Tests State Subclass """

    stat = State()

    def testClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.stat)), "<class 'models.state.State'>")

    def testStateInheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.stat, State)

    def testHasAttr(self):
        """test for user class attributes"""
        self.assertTrue(hasattr(self.stat, 'name'))
        self.assertTrue(hasattr(self.stat, 'id'))
        self.assertTrue(hasattr(self.stat, 'created_at'))
        self.assertTrue(hasattr(self.stat, 'updated_at'))

    def test_types(self):
        """test the type of attribute in user subclass"""
        self.assertIsInstance(self.stat.name, str)
        self.assertIsInstance(self.stat.id, str)
        self.assertIsInstance(self.stat.created_at, datetime.datetime)
        self.assertIsInstance(self.stat.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
