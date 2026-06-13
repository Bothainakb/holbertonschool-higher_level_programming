#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list containing positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 2, -3]), 5)

    def test_max_at_beginning(self):
        """Test when the maximum value is first."""
        self.assertEqual(max_integer([9, 4, 3, 2]), 9)

    def test_max_at_middle(self):
        """Test when the maximum value is in the middle."""
        self.assertEqual(max_integer([1, 8, 3, 2]), 8)

    def test_list_of_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.2, 3.5, 2.8]), 3.5)

    def test_identical_values(self):
        """Test a list with identical values."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
