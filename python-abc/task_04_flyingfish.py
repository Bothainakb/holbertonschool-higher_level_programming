#!/usr/bin/env python3
"""Module that defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """A fish."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """A bird."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish."""

    def fly(self):
        """Print flying fish flying message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swimming message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat message."""
        print("The flying fish lives both in water and the sky!")
