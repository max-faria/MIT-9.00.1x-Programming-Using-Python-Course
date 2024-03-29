# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:28:58 2023

@author: Max
"""
# Please read the Hangman Introduction before starting this problem. 
# We'll start by writing 3 simple functions that will help us easily code the 
# Hangman problem. First, implement the function isWordGuessed that takes in 
# two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
#This function returns a boolean - True if secretWord has been guessed 
#(ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

# Example Usage:

# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(isWordGuessed(secretWord, lettersGuessed))
# False
# For this function, you may assume that all the letters in secretWord and 
#lettersGuessed are lowercase.

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))