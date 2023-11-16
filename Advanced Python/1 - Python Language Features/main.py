# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:39:57 2022

@author: Januario Cipriano
"""

class myClass:
    def __bool__(self):
        return True
    
    def __len__(self):
        return 0
    

# my = myClass()
# print(bool(my))

x=[]
print(bool(x))
y = {}
print(bool(y))