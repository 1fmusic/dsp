#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:35:46 2017

@author: summer
"""
import csv

def get_dict(filename):
    deg = []
    aff = []
    email = []
    nam = []
    name = list()
    names ={} #create dictionary of last names and rows
    
    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
        
    for n in range(len(data)):
        person = data[n]
        nam.append(person[0])
        deg.append(person[1])
        aff.append(person[2])
        email.append(person[3])
        du = nam[n].split()
        name.append(du[len(du)-1])
   
    for i in range(len(name)): 
        names[name[i]] = names.get(name[i],[deg[i],aff[i],email[i]])

    return names
    