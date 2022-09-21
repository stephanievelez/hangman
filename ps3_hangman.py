# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from pickle import TRUE
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
    # FILL IN YOUR CODE HERE...
    letters_in_guessed=0
    while len(secretWord):
        for letter in secretWord:
            if letter in lettersGuessed:
                letters_in_guessed+=1
        
        if letters_in_guessed==len(secretWord):
            return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    letters_in_guessed=0
    guessed_word=''
    while len(secretWord):
        for letter in secretWord:
            if letter in lettersGuessed:
                letters_in_guessed+=1
                guessed_word+=letter
            else:
                guessed_word+=' _ '
        return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet=string.ascii_lowercase
    while True:
        if len(lettersGuessed)==0:
            return alphabet
        else:
            for letters in lettersGuessed:
                if letters in alphabet:
                    alphabet=alphabet.replace(letters, '') 
            return alphabet

    
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
    #mistakesMade: The number of incorrect guesses made so far.
    num_guess=8
    guess=''
    guessed=[]
    letterInWord=[]
    compare_guess=getGuessedWord(secretWord,guess)
    availableLetters=getAvailableLetters(guess) 
    print("Welcome to the game Hangman!" + "\n" + "I am thinking of a word that is", len(secretWord), "letters long.")
    print("-----------")   
    while True:
      print("You have", num_guess, " guesses left"+ "\n" + "Available letters:", availableLetters)
      guess=input("Please guess a letter: ")
      #compare_guess=getGuessedWord(secretWord, guess)
      if guess in guessed:
        print("Oops! You've already guessed that letter: ", compare_guess)
        print("-----------") 
      
      elif guess in getGuessedWord(secretWord, guess):
        letterInWord.append(guess)
        compare_guess=getGuessedWord(secretWord, letterInWord)
        print("Good guess: ", compare_guess)
        print("-----------") 
        checkWin=isWordGuessed(secretWord, compare_guess)
        if checkWin==True:
          return print("Congratulations, you won!")
         
      else:
        print("Oops! That letter is not in my word:" , compare_guess)
        print("-----------") 
        num_guess-=1
        if num_guess==0:
          checkWin=isWordGuessed(secretWord, compare_guess)
          if checkWin==True:
            return print("Congratulations, you won!")
          else: 
            return print("Sorry, you ran out of guesses. The word was", secretWord)
      guessed.append(guess)
      availableLetters=getAvailableLetters(guessed)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
