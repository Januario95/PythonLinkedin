#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:30:15  2022

@author: Januario Cipriano
"""

import json
import collections

def main():
    functions = {
        'namedtuple': 'Tuple with named fields',
        'OrderedDict-defaultdict': 'Dictionaries special properties',
        'Counter': 'Counts distinct values',
        'deque': 'Double-ended list object'
    }
    # print(json.dumps(functions, indent=4))
    
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10,20)
    p2 = Point(30,40)
    # print(p1, p2)
    # print(p1.x, p2.x)
    
    # TODO: USE _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)
    
    
if __name__=='__main__':
    main()
    






























