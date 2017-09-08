#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:35:46 2017

@author: summer
"""

import re

def unique_domains(emails):
    x = []
    domains = []
    
    for z in emails:
        z = z.strip('')
        domain = re.findall('@(\S.*)',z)
        x.append(domain)
    
    for i in x:    
        if i not in domains :
            domains.append(str(i))
        else :
            continue
    
    
    return domains
#    