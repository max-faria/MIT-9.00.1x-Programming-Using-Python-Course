# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:50:31 2023

@author: Max
"""

x = int(input('Enter a integer: '))
epsilon = float(input('Enter a epsilon value: '))
step = 0.1
numGuesses = 0
low = 1
high = x
ans =(low + high)/2.0

while abs(ans**2 - x) >= epsilon:
    if ans**2 < x:
        low = ans
    else:
        high = ans
    numGuesses += 1
    ans = (low+high)/2.0
    
print("Num of guesses" + str(numGuesses))
print(str(ans) + 'is the square root of: ' + str(x))
