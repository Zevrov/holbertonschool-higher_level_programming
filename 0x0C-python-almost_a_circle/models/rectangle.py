#!/usr/bin/python3
"""Model for Base"""
from models.base import Base


class Rectangle(Base):
    """Class for Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init for Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.int_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.int_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.int_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value):
        """Validates input"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """Area getter"""
        return self.__height * self.__width

    def display(self):
        """Displays the shape"""
        rect = "" + ' ' * self.__x
        rect = rect + str('#') * self.__width
        rect = '\n' * self.__y + '\n'.join(
                    list(rect for index in range(self.__height)))
        print(rect)

    def __str__(self):
        """returns information about the shape"""
        return "[Rectangle] ({:s}) {:s}/{:s} - {:s}/{:s}".format(self.__id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
