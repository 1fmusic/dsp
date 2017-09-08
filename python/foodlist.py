#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:54:33 2017

@author: summer
"""
from collections import defaultdict

food='spam spam spam'.split()

food_c=defaultdict(int)
for foo in food:
    food_c[foo] += 1
print(food_c)


import pprint as pp 

a={'first':123, 'fourth':{1:1, 3:2}}

print(a)
pprint.pprint(a)
pp.pprint(a, width=2)