#!/usr/bin/python3
""" Unit testing for Base class """

import sys
import unittest
from models import base
import models.base import Base

from io import StringIO
import sys

from models.rectangle import Rectangle
from models.square import Square

class BaseTest(unittest.TestCase):
    """ Class Base unittests"""

    def test_incrementation(self):
        """ obj id increments """
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_inputs(self):
        """checks for valid input """
        Base._Base__nb_objects = 0

        b_zero = Base()
        self.assertEqual(b_zero.id, 1)

        b_int = Base(17)
        self.assertEqual(b_int.id, 17)

        b_negint = Base(-29)
        self.assertEqual(b_negint.id, -29)
