#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:36:34  2022

@author: Januario Cipriano
"""

import string
import collections


def main():
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    
    # TODO: deques support the len() function
    # print('Item count: ', str(len(d)))
    
    # TODO: dequest can be iterated over
    # for elem in d:
    #     print(elem.upper(), end=',')
    
    # TODO: manupilate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    # print(d)
    
    # TODO: rotate the deque
    print(d)
    d.rotate(1)
    print(d)
    
if __name__=='__main__':
    main()
    






























