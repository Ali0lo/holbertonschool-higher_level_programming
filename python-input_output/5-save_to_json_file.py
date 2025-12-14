#!/usr/bin/python3
"""Module that defines a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to serialize to JSON
        filename (str): The name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
