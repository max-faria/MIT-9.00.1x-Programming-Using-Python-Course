# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:33:18 2023

@author: Max
"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    #Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
    #while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).
    if N<10:
        if N %10 == 7:
            return 1 
        else:
            return 0
    elif N %10 == 7:
        return 1 + count7(N//10)
    else:
        return 0 + count7(N//10)
    
         