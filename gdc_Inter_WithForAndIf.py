# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:48:55 2023

@author: Max
"""

def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 0
    testValue = min(a, b)
    
    for i in range (1, testValue + 1):
        if a %testValue == 0 and b %testValue == 0:
            gcd = testValue
        else:
            testValue -= 1
    return gcd
       