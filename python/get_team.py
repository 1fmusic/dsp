#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:06:31 2017

@author: summer
"""

def get_team(index_value, parsed_data):
    
    #for i in parsed_data :
    row = parsed_data[index_value]
    name = row[0]
    return name     