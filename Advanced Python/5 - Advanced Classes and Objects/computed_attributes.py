#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:52:11  2022

@author: Januario Cipriano
"""

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
        
    # TODO: use getattr do dynamically return a value
    def __getattr__(self, attr):
        if attr == "rbgcolor":
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue    
            )
        else:
            raise AttributeError(f'myColor class does not have {attr!r} attribute')
    
    # TODO: use setattr do dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)
    
    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rbgcolor", "hexcolor")


def main():
    # create an instance of myColor
    cls1 = myColor()
    
    # TODO: print the value of a computed attribute
    print(cls1.rbgcolor)
    print(cls1.hexcolor)
    
    # TODO: set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 85)
    print(cls1.rbgcolor)
    print(cls1.hexcolor)
    
    # TODO: access a regular attribute
    # print(cls1.red)
    
    # TODO: list the available attributes

    
    
if __name__=='__main__':
    main()
    






























