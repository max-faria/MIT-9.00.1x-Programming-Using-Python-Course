# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:10:43 2023

@author: Max
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a %b)
        