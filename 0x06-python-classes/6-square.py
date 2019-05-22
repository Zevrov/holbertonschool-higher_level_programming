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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple of int: the square's position on a plane

        The setter validates that the position is a tuple of 2 positive ints

        """

        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[1], int) and isinstance(value[0], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """Creates a square of a given size

        Size of the square is hidden

        Args:
            size (int): length of the sides
            position (tuple): the position of the square

        Raises:
            TypeError: size is not an integer
            ValueError: size is negative

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not(isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Returns the size of square

        Returns:
            size squared for area

        """

        return self.__size ** 2

    def my_print(self):
        """Prints out a grid of #'s representing the sqaure

        prints a blank line if size is 0

        also moves the sqaure to match position

        """

        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
