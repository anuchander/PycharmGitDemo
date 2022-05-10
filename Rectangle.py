class Rectangle:
    def __init__(self, height, width):
        self.__height=height
        self.__width=width

    def set_height(self, height):
        self.__height=height

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def area(self):
        return self.__height*self.__width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__height, self.__width)

    def __str__(self):
        return '{} - {}'.format(self.__height, self.__width)

rect1=Rectangle(20,30)
print(rect1)
print(repr(rect1))
print(str(rect1))
print(rect1.area())
