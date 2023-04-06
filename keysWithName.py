# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:19:23 2023

@author: Max
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary of keys and values as integers
    target: an integer
    '''
    result = []
    for key in aDict.keys():
        if aDict[key] == target:
            result.append(key)

    return sorted(result)
    
