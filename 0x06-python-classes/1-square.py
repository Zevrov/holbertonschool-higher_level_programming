#!/usr/bin/python3
"""The Square

Defining the class

"""


class Square:
    """A 2d square

    methods for maipulating it

    """

    def __init__(self, size):
        """Make a square of a given size

        Size of the new square is private

        Args:
            size (int): the length of the sides

        """

        self.__size = size
