# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:13:19 2023

@author: Max
"""

s='abcdefghijklmnopqrstuvwxyz'
longest =''
substring = ''

for index in range(len(s)):
    #if index == 0:
    #    sunstring = s[index]
    if s[index] >= s[index-1]:
        substring += s[index]
    else:
        substring = s[index]
    if len(substring) > len(longest):
        longest = substring

print('Longest substring on alphabetical order is:' + longest)
