# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:14:01 2022

@author: Januario Cipriano
"""

import requests
from requests.auth import HTTPBasicAuth


class LimitQuery:
    def __init__(self, func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        limit = args[0]
        if self.count < limit:
            self.func()
            self.count += 1
        else:
            print('No queries left!')

@LimitQuery
def query_api():
    auth = HTTPBasicAuth(username='januario095', 
                         password='Jaci1995')
    url = 'http://localhost:8000/api/items/'
    res = requests.get(url, auth=auth)
    print(res.status_code)


query_api(2)
query_api(2)
query_api(2)


















