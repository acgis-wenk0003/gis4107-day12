# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import math
def main():
    pass

def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass
#returns object id instead of value in the __str__ def for all shapes
class Circle(object):
    def __init__(self,radius):
        self.__radius=radius


    def area(self):
        area_of_the_circle=math.pi*(self.__radius**2)
        self.area=round(area_of_the_circle,5)
        return round (area_of_the_circle,5)


    def __str__(self):
        return "Circle area with a radius of "+str(self.__radius)+" is "+str(self.area)

class Square(object):
    def __init__(self,side):
        self.__side=side
        self.area



    def area(self):
        area_of_the_square= self.__side**2
        return round(area_of_the_square,5)
        self.area=area_of_the_square

    def __str__(self):
        return "Square area with a side of "+str(self.__side)+' is '+str(self.area())
#onto the rectangle issue

class Rectangle(object):
    def __init__ (self,width,height):
        self.__width=width
        self.__height=height
        self.area

    def area(self):
        Area_of_the_rect= self.__width * self.__height
        return Area_of_the_rect
        self.area=Area_of_the_rect

    def __str__(self):
        return "Rectangle area with a width of "+ str(self.__width)+" and a height of "+str(self.__height)+" is "+str(self.area())
if __name__ == '__main__':
    main()