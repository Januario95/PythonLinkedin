#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:58:46  2022

@author: Januario Cipriano
"""

# TODO: define a funciton that takes variable arguments
def addition(base, *args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    # TODO: pass difference arguments
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))
    
    # TODO: pass an existing list
    myNums = [5,10,15,20]
    print(addition(*myNums))
    
if __name__=='__main__':
    main()
    
























