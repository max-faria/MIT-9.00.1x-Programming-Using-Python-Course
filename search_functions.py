# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:29:49 2023

@author: Max
"""

def search(L,e):
    for i in range(len(L)): #the code runs trwoght all the list searching for the number
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e): #only return corret values for len(L) = 0 or 1
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def bisec_search1(L,e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisec_search1(L[:half], e)   
        else:
            return bisec_search1(L[half:], e)
        
def bisec_search2(L,e):
    def bisec_searchhelper(L,e,low,high):
        if high == low:
            return L[0] == e
        mid = (high + low)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing to search
                return False
            else: 
                return bisec_searchhelper(L, e, low, mid-1)
        else:
            return bisec_searchhelper(L, e, mid+1, high)
        
    if len(L) == 0:
        return False
    else:
        return bisec_searchhelper(L, e, 0, len(L) - 1) #len(L)-1 because of the maximum index of L 
        
testlist = [1,2,3,4,5,6,9]
print(search(testlist,8))
print(newsearch(testlist, 2))