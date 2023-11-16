#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:02:11  2022

@author: Januario Cipriano
"""

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # use @unique to allow unique values for the constants
    # RED_DELICIOUS = 1
    # use auto() to allow automatic value counting
    PEAR = auto()


def main():
    # TODO: enums have human-readable values and types
    # print(Fruit.APPLE)
    # print(type(Fruit))
    # print(type(Fruit.APPLE))
    # print(repr(Fruit.APPLE))
    
    # TODO: enums have name and value properties
    # print(Fruit.APPLE.name, Fruit.APPLE.value)
    
    # TODO: print the auto-generated value
    print(Fruit.PEAR.name, Fruit.PEAR.value)
    
    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])
    
if __name__=='__main__':
    main()
    






























