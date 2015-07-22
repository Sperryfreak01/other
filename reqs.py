# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:02:08 2015

@author: Pete
"""

import requests

url = 'https://maps.googleapis.com/maps/api/directions/json'
query = {'origin': 'Toronto', 'destination': 'Montreal', 'key':'AIzaSyAfY4klBTbZf16oY_hcRcH2Cr4XjEFhJHI'}

r = requests.get(url, params = query)
print (r.status_code)