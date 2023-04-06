# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:48:22 2023

@author: Max
"""

def deep_reverse(L):
    """
    

    Parameters
    ----------
    L : list of lists
    Take all the elements of L and reverse it.
    Returns nothing
   

    """
    #or i in L:
    L.reverse()
    #a=[]
    for i in range(len(L)):
        L [i] = (L[i][::-1])
    #return L

L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))        