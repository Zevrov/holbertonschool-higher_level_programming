#!/usr/bin/python3
"""The Square

definition of the square

"""


class Square:
    """a 2d square

    methods for manipulating it

    """

    def __init__(self, size=0):
        """Creates a square of a given size

        Size of the square is hidden

        Args:
            size (int): length of the sides

        Raises:
            TypeError: size is not an integer
            ValueError: size is negative

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the size of square

        Returns:
            size squared for area

        """

        return self.__size ** 2
