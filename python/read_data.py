#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:35:46 2017

@author: summer
"""
import re 
import csv

def count_degrees(filename):
    
    deg = list()
    degs = list()
    degrees ={} #create dictionary of degrees and counts
    
    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
        
    for n in range(len(data)):
        person = data[n]
        degs.append(person[1])
            
    # split up lines with more than 1 degree
    for z in range(len(degs)):
        x = degs[z].split()
        for n in range(len(x)):
            deg.append(x[n])    
            
      
    for i in range(len(deg)):    
        if not  re.search('[P][h]',deg[i]) == None :
            degrees['PhD'] = degrees.get('PhD',0) + 1
        elif not re.search('[M].*[S]',deg[i]) == None:
            degrees['MS'] = degrees.get('MS',0) + 1        
        elif not re.search('^[B]',deg[i]) == None:
            degrees['BSED'] = degrees.get('BSED',0) + 1     
        elif not re.search('[S]',deg[i]) == None :
            degrees['SCD'] = degrees.get('SCD',0) + 1
        elif not re.search('[M].*[D]',deg[i]) == None :
            degrees['MD'] = degrees.get('MD',0) + 1
        elif not re.search('[M].*[P]',deg[i]) == None:
            degrees['MPH'] = degrees.get('MPH',0) + 1
        elif not re.search('[J].*[D]',deg[i]) == None :
            degrees['JD'] = degrees.get('JD',0) + 1   
        elif not re.search('[M].*[A]',deg[i]) == None:
            degrees['MA'] = degrees.get('MA',0) + 1    
        elif not re.search('[0]',deg[i]) == None:
            degrees['0'] = degrees.get('0',0) + 1 
        

    return degrees
    