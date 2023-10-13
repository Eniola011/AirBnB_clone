#!/usr/bin/python3
"""Unittest for State Module"""


import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Tests State Subclass """

    state = State()

    def testClass(self):
        """tests subclass"""
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def testStateInheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, State)

    def testHasAttr(self):
        """test for user class attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_types(self):
        """test the type of attribute in user subclass"""
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
