#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:38:16 2017

@author: summer
"""



def get_ind(goal):

    scores = list()    
    for i in range(len(goal)):
        row = goal[i]
        x=abs(int(row[5])-int(row[6]))
        scores.append(x)
    
    mm = min(scores)
    indexMin = scores.index(mm)    
    return indexMin