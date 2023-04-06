# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:26:36 2023

@author: Max
"""

# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation of 
#integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., 
# corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     #YOUR CODE HERE
# Paste your entire function, including the definition, in the box below. 
#Do not leave any debugging print statements.



def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    if k < 0:
        return False
    n = 1
    soma = 0
    # the triangular number is a sum of numbers
    while soma < k:
        soma = soma + n
        if soma == k:
            print(n)
            print(soma)
            return True
        else:
            n += 1
    return False