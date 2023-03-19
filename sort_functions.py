# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:45:32 2023

@author: Max
"""

# def bogo_sort(L):
#     while not is_sorted(L):
#         random.shuffle(L)
        
def bubble_sort(L):
    """
    inner for loop is for doing the comparisons
    outer while loop is for doing multiple passes
    until no more swaps
    
    this function compares two values em put them in order

    """
    swap = False
    while not swap:
        swap = True
        for j in range (1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selection_sort(L):
    """

    divide the values in two and then compares
    the first one with the last one of the suffix
    and then order. The suffix grws in each loop    

    """
    suffixSt = 0
    while suffixSt != len(L):
        for i in range (suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
            
def merge(left,right):
    """
    

    compares the first element of each list
    the smaller one will be added to the result list.
    the result list is then already sorted.
    
    left, right: lists

    """
    result = []
    i,j = 0,0
    if i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append[i]
            i += 1
        else:
            result.append[j]
            j += 1
    while (i < len(left)):
        result.append[left[i]]
        i += 1
    while (j < len(right)):
        result.append(right[j])
        return result
    
def merge_sort(L):
    """
    divide on list in two and then apply merge

    Parameters
    ----------
    L : list of n elements.

    Returns
    -------
    sorted L.

    """
    if len(L) == 0:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left,right)
    
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)): #if take off i+i the list is sorted in decreasing order
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
testlist=[2,6,7,4,9,0]

print(swapSort(testlist))
    
        