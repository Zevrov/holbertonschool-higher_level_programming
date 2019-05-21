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

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
	def area(self):
		return self.__size ** 2
