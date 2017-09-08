#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:35:46 2017

@author: summer
"""

import csv

def emails(filename):
    
    emails = list()
        
    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
        
    for n in range(len(data)):
        person = data[n]
        emails.append(person[3])
        
    return emails
    