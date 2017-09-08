#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:10:50 2017

@author: summer
"""
import csv

def write_to_csv(list_of_emails):
    with open("emails.csv","w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('emails',))
        for row in list_of_emails:
            writer.writerow((row,))
        
        