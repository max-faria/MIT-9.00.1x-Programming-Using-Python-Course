# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:47:01 2023

@author: Max
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
       return aList
    elif isinstance(aList[0], list):
       return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])


aList= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))