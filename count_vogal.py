# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:21:14 2023

@author: Max
"""

#Count of vowels
s='azcbobobegghakl'

count=0
for letter in s:
    if letter == 'a' or letter == 'e' or letter =='i' or letter =='o' or letter == 'u':
        count += 1
print(count)
    