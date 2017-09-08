# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    
    if int(count) >= 10  :
        return 'Number of donuts: many'
    else :
       return 'Number of donuts: %s' %(count)

    
def both_ends(s):
    
    if len(s) >= 2 :
        ss = s[0:2] + s[-2:]
        return ss
    else :
        return '' 
    
def fix_start(s):
    f = s[0]
    ss = ''
    cc = 0
    if s.count(f) > 1:
        for n in s :
            if cc == 0 :
                ss = f
                cc = cc +1
            elif n != f :
                ss = ss + n
            else :
                ss = ss + '*'
        return ss
    else: 
        return s
    


def mix_up(a,b):
    a1 = b[0:2] + a[2:]
    b1 = a[0:2] + b[2:]
    return a1 + ' ' + b1
    


def verbing(s):
    
    if len(s) >= 3 and 'ing' not in s :
        ss = s + 'ing'
    elif len(s) >=3 and 'ing' in s :
        ss = s + 'ly'
    else :
        ss = s
        
    return ss
   
import re 

def not_bad(s):
    
    if  re.search('not.*bad', s) == [] :
        ss = s
    else :    
        ss = re.sub('not.*bad','good',s)

    return ss    
   


def front_back(s1,s2):
    
    y = len(s1) % 2
    y1 = len(s1)//2
    z = len(s2) % 2
    y2 = len(s2) // 2
    
    if y == 0:
        aFro = s1[:y1]
        aBak = s1[y1:]
    else :
        aFro = s1[:y1+1]
        aBak = s1[y1+1:]
    
    if z == 0:
        bFro = s2[:y2]
        bBak = s2[y2:]
    else :
        bFro = s2[:y2+1]
        bBak = s2[y2+1:]
    
    return aFro + bFro + aBak + bBak