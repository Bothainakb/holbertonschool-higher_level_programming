#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the instance."""
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance."""
        for key, value in json.items():
            setattr(self, key, value)
