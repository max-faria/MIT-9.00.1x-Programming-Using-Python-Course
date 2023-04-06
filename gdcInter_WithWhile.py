# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:37:21 2023

@author: Max
"""

def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
