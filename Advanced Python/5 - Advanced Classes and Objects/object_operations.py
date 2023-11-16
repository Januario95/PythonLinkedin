#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:47:04  2022

@author: Januario Cipriano
"""

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)
    
    def raise_on_error(self, other):
        if not isinstance(other, Point):
            raise TypeError('Can only add points together')
    
    # TODO: implement addition
    def __add__(self, other):
        self.raise_on_error(other)
        return Point(self.x + other.x, self.y + other.y)
    
        # if isinstance(other, Point):
        #     return Point(self.x + other.x, self.y + other.y)
        # raise TypeError('Can only add points together')
    
    # TODO: implement subtraction
    def __sub__(self, other):
        self.raise_on_error(other)
        return Point(self.x - other.x, self.y - other.y)
        
        # if type(other) == Point:
        #     return Point(self.x - other.x, self.y - other.y)
        # raise TypeError('Can only subtract points together')
    
    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    # DEclare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    # print(p1, p2)
    
    # TODO: Add two points
    p3 = p1 + p2
    # print(p3)
    
    # TODO: substract two points
    p4 = p3 - Point(3, 5)
    # print(p4)
    
    # TODO: Perform in-place addition
    print(p1)
    p1 += p2
    print(p1)
    
    
if __name__=='__main__':
    main()
    






























