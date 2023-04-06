# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:11:09 2023

@author: Max
"""

increment=0.001
epsilon=0.000001
cube=27
guess=0.0
num_guesses=0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_gueses: ', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Could't find the perfect cube")
print("The perfect cube for", cube, "is: ", guess)

    