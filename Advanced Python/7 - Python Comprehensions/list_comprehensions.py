#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:00:00  2022

@author: Januario Cipriano
"""


def main():
    # print([(t*9/5)+32 for t in [32, 65, 104, 212]])
    
    # define two lists of numbers
    evens = [2,4,6,8,10,12,14,16,18,20]
    odds = [1,3,5,7,9,11,13,15,17,19]
    
    # TODO: Perfom a mapping and filter function to a list
    # evenSquared = list(
    #     map(lambda e: e**2, 
    #         filter(lambda e: e>4 and e<16, evens)))
    # print(evenSquared)
    
    # TODO: Derive a new list of numbers from a given list
    evenSquared = [e**2 for e in evens if e>4 and e<16]
    # print(evenSquared)
    
    # TODO: Limit the items operated on with a predicate condition
    oddSquared = [e**2 for e in odds if e>3 and e<17]
    print(oddSquared)
    
if __name__=='__main__':
    main()
    






























