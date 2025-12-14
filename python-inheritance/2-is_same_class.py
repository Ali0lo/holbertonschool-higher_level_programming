#!/usr/bin/python3
"""Module that defines an is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
