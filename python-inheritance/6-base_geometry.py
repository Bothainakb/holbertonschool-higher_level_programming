#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
