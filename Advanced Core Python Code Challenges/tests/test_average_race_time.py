# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:39:41 2022

@author: Januario Cipriano
"""

from ..find_runner_avg_race_time import *

def test_rhine_times():
	result = get_rhines_times()
	expected = ['32:32.6', '33:04', '33:21', '33:25',
				'33:30', '33:31']
	assert result == expected

def test_average_race_time():
	result = get_average()
	expected = '33:13.8'
	assert result == expected

