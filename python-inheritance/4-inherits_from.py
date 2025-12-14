#!/usr/bin/python3
"""Module that defines an inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class

    Args: 
        obj: The object to check
        a_class: The class to compare against

    Returns: 
        True if obj is an instance of a class that inherited from a_class,
        False otherwise (including if obj is exactly an instance of a_class)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
