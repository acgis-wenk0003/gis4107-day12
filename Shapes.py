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
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        self.__radius=radius
    @property
    def area(self):
        return self.area


    def area(self):
        area_of_the_circle=math.pi*(self.__radius**2)
        self.area=round(area_of_the_circle,5)
        return round (area_of_the_circle,5)


    def __str__(self):
        return "Circle area with a radius of "+str(self.__radius)+" is "+str(self.area)

class Square(object):

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        self.__side=side
    @property
    def area(self):
        return self.area

    def area(self):
        area_of_the_square= self.__side**2
        return round(area_of_the_square,5)
        self.area=area_of_the_square

    def __str__(self):
        return "Square area with a side of "+str(self.__side)+' is '+str(self.area())
#onto the rectangle issue

class Rectangle(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width=width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height=height
    @property
    def area(self):
        return self.area

    def area(self):
        Area_of_the_rect= self.__width * self.__height
        return Area_of_the_rect
        self.area=Area_of_the_rect

    def __str__(self):
        return "Rectangle area with a width of "+ str(self.__width)+" and a height of "+str(self.__height)+" is "+str(self.area())
if __name__ == '__main__':
    main()