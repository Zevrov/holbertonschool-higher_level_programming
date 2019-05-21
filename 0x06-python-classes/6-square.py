#!/usr/bin/python3
class Square:

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		if not isinstance(value, int)
			raise TypeError("size must be an integer")
	    if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, value):
		if type(value) != tuple or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		if not isinstance(val[0], int) or not isinstance(val[1], int):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

	def area(self):
		return self.__size ** 2

	def my_print(self):
		if self.__size == 0:
			print()
			return
		for i in range(self.__size):
			print("#" * self.__size)
