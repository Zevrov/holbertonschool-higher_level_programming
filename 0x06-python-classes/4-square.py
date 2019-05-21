#!/usr/bin/python3
"""The Square

definition of the square

"""


class Square:
    """a 2d square

    methods for manipulating it

    """

    @property
    def size(self):
        """int: length of square sides

        The setter validates that the size is an integer and is 0 or greater

        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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
