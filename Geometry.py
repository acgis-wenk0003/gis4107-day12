# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Chris Wenkoff
#
# Created:     22/12/2017
# ------------------------------------------------------------------------------

def main():
    pass

class Point(object):
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)


class Line(object):
    def __init__(self,fromPoint,toPoint):
        str_fromPoint=str(fromPoint).split(',',1)
        str_toPoint=str(toPoint).split(',',1)
        self.fromPoint=Point(str_fromPoint[0],str_fromPoint[1])
        self.toPoint=Point(str_toPoint[0],str_toPoint[1])
        self.__length=0


    def length(self):
        length_of_the_line= ((self.toPoint.x-self.fromPoint.x)**2+(self.toPoint.y-self.fromPoint.y)**2)**0.5
        self.__length=length_of_the_line
        return round(self.__length,5)

#need to complete polyline
class Polyline(object):
    def __init__(self):
        self.__segments=[]
        self.__length=float()

    def addSegment(self,segment):
        if type(segment) is Line:
            Llength=segment.length()
            self.__segments.append(Llength)

        else:
            print "Incorrect Type must be Line."

    def length(self):
        total_length=float()
        for segmen in self.__segments:
            total_length+=segmen
        self.__length=total_length
        return round(total_length,5)



if __name__ == '__main__':
    main()