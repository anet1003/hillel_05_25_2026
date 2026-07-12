import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side **2

    def perimeter(self):
        return self.__side * 4



class Rectangle(Figure):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return  2 * (self.__width + self.__height)



class Circle(Figure):

    def __init__(self, radius):
        self.__radius = radius


    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


figures = [
    Square(5),
    Rectangle(4,6),
    Circle(3)
]

for figure in figures:
    print("Area:",figure.area())
    print("perimeter:", figure.perimeter())

