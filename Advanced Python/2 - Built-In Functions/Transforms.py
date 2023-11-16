#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:17:39  2022

@author: Januario Cipriano
"""

def filterFunc(x):
    # if x % 2 == 0:
    #     return False
    # return True
    return x % 2 != 0

def filterFunc2(x):
    # if x.isupper():
    #     return False
    # return True
    return x.islower()

def filterFunc3(x):
    # if x.islower():
    #     return False
    # return True
    return x.isupper()

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >= 80 and x < 90:
        return 'B'
    elif x >= 70 and x < 80:
        return 'C'
    elif x >= 65 and x < 70:
        return 'D'
    else:
        return 'F'

def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = 'abcDeFGHiJklmnoP'
    grades = (81, 89, 94, 78, 61, 66, 99, 74)
    
    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    # print(odds)
    
    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    # print(lowers)
    
    uppers = list(filter(filterFunc3, chars))
    # print(uppers)
    
    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    # print(squares)
    
    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(dict(zip(grades, letters)))


if __name__=='__main__':
    main()
















