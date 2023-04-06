# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:06:25 2023

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
      return True
   
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   
   if char == midChar:
       return True
   elif char < midChar:
       return isIn(char, aStr[:midIndex])
   else:
       return isIn(char, aStr[midIndex+1:])