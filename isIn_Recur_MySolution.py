# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:14:35 2023

@author: Max
"""

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   if aStr =='':
      return False
   if len(aStr) == 1:
       return aStr == char
  
   low = 0
   high = len(aStr)
   midChar = aStr[(low + high)//2]
   
   if midChar == char:
      return True
   elif char < midChar:
       return isIn(char, aStr[:((low + high)//2)])
   else:
       return isIn(char, aStr[((low + high)//2)+1:])

print(isIn('z', 'abefgllqstwxyzz'))         