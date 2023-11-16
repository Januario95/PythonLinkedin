# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:43:21 2022

@author: Januario Cipriano
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path='C:\\Users\\a248433\\Documents\\drivers\\chromedriver.exe',
                          options=options)
driver.maximize_window()

driver.get('http://localhost:8000/color_picker/')

count = 500
while count > 0:
    convert_color = driver.find_element(By.XPATH, '/html/body/div/div/div/div/input[4]')
    convert_color.click()
    
    generate_color = driver.find_element(By.XPATH, '/html/body/div/div/div/div/input[5]')
    generate_color.click()
    count -= 1


def check_value(val):
    if val >= 0 and val <= 255:
        return val
    raise TypeError('Color value must be between 0 and 255 incluvise')


class myColor:
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
            self.red = check_value(val[0])
            self.green = check_value(val[1])
            self.blue = check_value(val[2])
        else:
            super().__setattr__(attr, val)
    
    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rbgcolor", "hexcolor")

cls1 = myColor()
# print(cls1)
# print(cls1.rbgcolor)
# print(cls1.hexcolor)


# cls1.rgbcolor = (125, 255, 85)
# print(cls1.rbgcolor)
# print(cls1.hexcolor)      











































