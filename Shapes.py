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

class Circle(object):
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        self.__radius=radius


    def area(self):
        area_of_the_circle= math.pi*(self.__radius**2)
        return str(round(area_of_the_circle, 5))


    def __str__(self):
        return "Circle area with a radius of "+str(self.__radius)+" is "+str(self.area)

class Square(object):
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        self.__side=side

    def area(self):
        area_of_the_square= self.__side**2
        return round(area_of_the_square,5)
        self.area=area_of_the_square

    def __str__(self):
        return "Square area with a side of "+str(self.__side)+ ' is '+str(self.area)



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

    def area(self):
        Area_of_the_rect= self.__width * self.__height
        return Area_of_the_rect

if __name__ == '__main__':
    main()