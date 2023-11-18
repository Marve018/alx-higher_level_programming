#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        A child class from unittest class
    """
    def test_negative(self):
        """
            the class method
        """
        self.assertAlmostEqual(max_integer([-1, 0, -100]), 0)
        self.assertAlmostEqual(max_integer([2.8, 8.9, 8, 0]), 8.9)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
