#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:42:05  2022

@author: Januario Cipriano
"""

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    
    # use a dictionary to count each element
    # fruitCounter = {}
    # fruitCounter = defaultdict(int)
    fruitCounter = defaultdict(lambda: 100) # starting count value
    
    # Count the elements in the list
    # for fruit in fruits:
    #     if fruit in fruitCounter.keys():
    #         fruitCounter[fruit] += 1
    #     else:
    #         fruitCounter[fruit] = 1
            
    # use defaultdict to count each element
    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1
    
    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ':' + str(v))
    
    
if __name__=='__main__':
    main()
    






























