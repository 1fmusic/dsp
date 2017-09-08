# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Sadly, I only put this one into hacker rank and submitted it before I realized I needed to add it here. 

    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    raise NotImplementedError


def front_x(words):

    y = list()
    yy = list()
    for xx in words :
        if xx.startswith('x') == True :
            y.append(xx) 
                     
        else :
           yy.append(xx)
    yy.sort() 
    y.sort()              
    return (y  + yy)  
    


def sort_last(tuples):
    
    def last_item(y):
        return y[-1]

    xx = sorted(tuples, key=last_item)
        
    return xx



nums = [2,2, 3,3,3,3]
def remove_adjacent(nums):
    y = len(nums)
    cot = 0
    for i in range(y-1) :
        if  nums[cot]  == nums[cot + 1] :
            nums.pop(cot)       
        else :
            cot = cot +1
                  
    return nums



import itertools 

def linear_merge(list1,list2):
    
    blist = list(itertools.chain(list1,list2))
    blist.sort()
    
    return blist