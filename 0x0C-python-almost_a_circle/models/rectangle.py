#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validation("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validation("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "height" or name == "width") and value < 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value <= 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        return self.__height * self.__width

    def display(self):
        rect = "" + ' ' * self.__x
        rect += str('#') * self.__width
        rect = '/n' * self.__y + '/n'.join(
                    list(rect for index in range(self.__height)))
        print rect

    def __str__(self):
        return "[Rectangle] ({:s}) {:s}/{:s} - {:s}/{:s}".format(self.__id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
