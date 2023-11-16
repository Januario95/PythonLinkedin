#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:38:13  2022

@author: Januario Cipriano
"""


def main():
    # Use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    
    # TODO: all will return true only if all values are true
    print(all(list1))
    
    # TODO: min and max will return minimum and maximum values in a sequence
    print('min:', min(list1))
    print('max:', max(list1))
    
    # TODO: use sum() to sum up all of the values in a sequence
    print('sum:', sum(list1))

if __name__=='__main__':
    main()

