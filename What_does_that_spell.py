# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:49:25 2023

@author: Max
"""
ans = 'aefhilmnorsxAEFHILMNORSX'

word = input('Enter a name: ')
times = int(input( 'Enter a integrer: '))
i=0

while i < len(word):
    char = word[i]
    if char in ans:
        print("Give me a: " + char + "!" +  char)
    else:
        print("Give me an: " + char + "!" +  char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word,  "!!!")
    
