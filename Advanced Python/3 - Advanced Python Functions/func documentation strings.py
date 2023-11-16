#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:24:46  2022

@author: Januario Cipriano
"""

def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2) -> Doesn't really do anything, just prints.
    
    Parameters:
        arg1: the first argument. Whatever you feel like passing.
        arg2: second argument. Defaults to None
    """
    print(arg1, arg2)


def main():
    # print(map.__doc__)
    # print(print.__doc__)
    # print(collections.__doc__)
    print(myFunction.__doc__)
    
    
if __name__=='__main__':
    main()
    
























