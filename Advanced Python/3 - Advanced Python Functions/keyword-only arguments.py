#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:21:06  2022

@author: Januario Cipriano
"""

def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, suppressExceptions=True)
    
if __name__=='__main__':
    main()
    






























