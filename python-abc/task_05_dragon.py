#!/usr/bin/env python3
"""Module that defines mixins and the Dragon class."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
