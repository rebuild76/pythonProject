import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, deck_a):
        self.a = deck_a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, radius):
        self.r = radius
    def get_circle_area(self):
        return math.pi * self.r ** 2