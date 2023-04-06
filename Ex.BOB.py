# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:52:39 2023

@author: Max
"""

s='azcbobobegghakl'
count = 0
for n in range(len(s)):
    if s[n:n+3] == "bob":
        count += 1

print("Number of times bob occurs is:" + str(count))