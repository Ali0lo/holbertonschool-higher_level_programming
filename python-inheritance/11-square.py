#!/usr/bin/python3
"""Module that defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square with size

        Args:  
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
