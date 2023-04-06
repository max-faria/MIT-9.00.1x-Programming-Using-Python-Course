# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([char if char in lettersGuessed else "_"  for char in secretWord ])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ''
    for char in string.ascii_lowercase:
     if char not in lettersGuessed:
       result = result + char
    return result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # secretWord = chooseWord(wordlist)
    # lettersGuessed = []
    # guesses = 8

    # print('Welcome to the Game Hangman!')
    # print('I am thinking of a word that is', len(secretWord), 'letters long.')
    # print('-------------')
    # print('You have 8 guesses left.')
    # print('Available Letters:' + getAvailableLetters(lettersGuessed))
    secretWord = chooseWord(wordlist)
    lettersGuessed = []
    print('Welcome to the Game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    guesses = 8
    
    while guesses >= 1:
        # letter = str(input('Please guess a letter: '))
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('-------------')
            return print('Congratulations, you won!')
            break
        
        # if secretWord == getGuessedWord(secretWord, lettersGuessed):
        #     print('-------------')
        #     return print('Congratulations, you won!')
        #     break
        else:
            print('-------------')
            print('You have ' + str(guesses) + ' guesses left.')
            print('Available Letters:' + getAvailableLetters(lettersGuessed))
            letter = str(input('Please guess a letter: '))
        
            if letter in secretWord and letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print('Good Guess:' ,getGuessedWord(secretWord, lettersGuessed))
            
            # print("Oops! That letter is not in my word:" , getGuessedWord(secretWord, lettersGuessed))
            # return  print('Sorry, you ran out of guesses. The word was else.')
        
            elif letter in lettersGuessed:
                print("Oops! You've already guessed that letter:" , getGuessedWord(secretWord, lettersGuessed))
            # print('-------------')
            # print('You have ' + str(guesses) + ' guesses left.')
            # print('Available Letters:' + getAvailableLetters(lettersGuessed))
           
        # elif letter in secretWord:
        #     lettersGuessed.append(letter)
        #     print('Good Guess:' ,getGuessedWord(secretWord, lettersGuessed))
        #     print('-------------')
        #     print('You have ' + str(guesses) + ' guesses left.')
            
            elif letter not in secretWord:
                guesses -= 1
                lettersGuessed.append(letter)
                print("Oops! That letter is not in my word:" , getGuessedWord(secretWord, lettersGuessed))
            # print('-------------')
            # print('You have ' + str(guesses) + ' guesses left.')
            # print('Available Letters:' + getAvailableLetters(lettersGuessed))
            
        if guesses == 0:
            print('-------------')
            return  print('Sorry, you ran out of guesses. The word was else.')
        else:
            continue                    
            

secretWord = chooseWord(wordlist)
print(hangman(secretWord))
# lettersGuessed = []
# print('Welcome to the Game Hangman!')
# print('I am thinking of a word that is', len(secretWord), 'letters long.')
# print('-------------')
# print('You have 8 guesses left.')
# print('Available Letters:' + getAvailableLetters(lettersGuessed))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
