#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:26:12  2022

@author: Januario Cipriano
"""

import logging

# To capture loggings in a file,
# run the script in cmd

def main():
    # TODO: Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename='output.log',
                        # override file every on every call
                        filemode='w' 
                        )
    
    # Try out each of the log levels
    logging.debug('This is debuging message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    
    # Ouput formatted strings to the log
    logging.info("Here's a {} variable and an int:".format(
        "string", 10 
    ))
    
    
if __name__=='__main__':
    main()
    






























