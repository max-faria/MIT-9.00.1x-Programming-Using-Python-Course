# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:53:10 2023

@author: Max
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc_count = 0   #count the position of the highest of numeber in increasing order
    dec_count = 0    #count the position of the highest numver in decreasing order
    result = 0      # count the position of the last number of the highest inc ou dec order
    maxcount = 0    #
    
    for i in range (len(L) - 1):
        if L[i] <= L[i+1]:
            inc_count += 1
            print('increasing')
            if inc_count > maxcount:
                inc_count = maxcount
                result = i + 1
        else:
            inc_count = 0
        
        if L[i] >= L[i+1]:
            dec_count += 1
            print('decreasing')
            if dec_count > maxcount:
                dec_count = maxcount
                result = i + 1
        else:
            dec_count = 0
            
    print(result)
    print(maxcount)
    startposition = result - maxcount
    return sum(L[startposition:result +1])
            