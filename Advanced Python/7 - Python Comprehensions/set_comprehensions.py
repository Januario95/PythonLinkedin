#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:21:00  2022

@author: Januario Cipriano
"""


def main():
    # define a list of temperature data points
    # ctemps = [5,10,12,14,10,23,41,30,12,24,12,18,29]
    # ftemps1 = [(t*9/5)+32 for t in ctemps]
    # ftemps2 = {(t*9/5)+32 for t in ctemps}
    # print(ftemps1)
    # print(ftemps2)
    
    # TODO: build a set of unique Fahrenheit temperatures
    
    # TODO: build a set from an input source
    sTemp = 'The quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(len(chars))
    print(sorted(chars))
    
if __name__=='__main__':
    main()
    






























