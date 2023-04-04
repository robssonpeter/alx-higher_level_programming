#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_function_works(self):
        self.assertAlmostEqual(max_integer([5, 10, 15, 25]), 25)
