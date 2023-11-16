# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:55:08 2022

@author: Januario Cipriano
"""

import logging

extData = {
    'user': 'joedoe@example.com'
}


def anotherFunc():
    logging.debug('This is a debug-level messae',
                  extra=extData)

def main():
    fmtstr = 'User:%(user)s:%(asctime)s:%(name)s:%(levelname)s:%(message)s:%(funcName)s:%(lineno)d'
    datestr = '%d-%b-%Y %I:%M %p'
    logging.basicConfig(filename='config.log',
                        level=logging.DEBUG,
                        filemode='w',
                        format=fmtstr,
                        datefmt=datestr)
    
    logging.info('This is an info-level log message',
                  extra=extData)

if __name__=='__main__':
    main()
    
    

















































