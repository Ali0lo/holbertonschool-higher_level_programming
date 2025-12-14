#!/usr/bin/python3
"""Module that defines a write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of characters

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
