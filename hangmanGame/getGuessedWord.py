# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:03:54 2023

@author: Max
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #string = ""
    return ''.join([char if char in lettersGuessed else "_"  for char in secretWord ])
    # for char in secretWord:
    #     if char in lettersGuessed:
    #         string += char
    #     else:
    #         string += "_"
    # return string

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
    