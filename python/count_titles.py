#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:35:46 2017

@author: summer
"""
import re 
import csv

def count_titles(filename):
    

    tits = list()
    titles ={} #create dictionary of degrees and counts
    
    with open(filename,'r') as fb :
        reader = csv.reader(fb, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
        
    for n in range(len(data)):
        person = data[n]
        tits.append(person[2])
      
    for i in range(len(tits)):    
        if not  re.search('[A][s][s][o].*',tits[i]) == None :
            titles['Associate Professor of Biostatistics'] = titles.get('Associate Professor of Biostatistics',0) + 1
        elif not re.search('^[P].*',tits[i]) == None:
            titles['Professor of Biostatistics'] = titles.get('Professor of Biostatistics',0) + 1        
        elif not re.search('[A][s][s][i].*',tits[i]) == None:
            titles['Assistant Professor of Biostatistics'] = titles.get('Assistant Professor of Biostatistics',0) + 1     

    return titles
    