#!/usr/bin/python3
"""add attribute module"""


def add_attribute(mc, name, value):
    """add attribute """
    if not name or not value:
        raise TypeError("can't add new attribute")
    if hasattr(mc, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(mc, name, value)
