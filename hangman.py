import random
import sys
from itertools import chain

hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fileName = "mit.edu_~ecprice_wordlist.10000.txt"
display = []
livesLost = 0
wrongGuesses = []

def get_random_word():
    with open(fileName, 'r') as file:
        words = file.read().split()
        #cuts off words shorter then 3 letters
        words = [word.strip() for word in words if len(word.strip()) >= 3]

        return random.choice(words)    

def check_for_win():
    return any(element == "_" for element in display)

def check_for_guess_used(guessAttempted):
    return any(element == guessAttempted for element in chain(display, wrongGuesses))

def display_hangman():
    print(hangman[livesLost])

activeWord = get_random_word()

for letter in activeWord:
    display += "_"

print(display)
while(check_for_win() == True):
    guess = input("Guess a letter: ").lower()
    while len(guess) != 1 or not guess.isalpha() or check_for_guess_used(guess):
        if check_for_guess_used(guess):
            guess = input("Can't guess the same letter twice: ")
        else:
            guess = input("Guess must be one letter:")

    displayBeforeChange = display.copy()
    
    for position in range(len(activeWord)):
        letter = activeWord[position]
        if letter == guess:
            display[position] = letter

    if displayBeforeChange == display:
        print("Bad Guess!")
        livesLost = livesLost + 1
        wrongGuesses += guess
    else:
        print("Good Guess!")
    
    display_hangman()
    print(display)
    print(f"Incorrect guesses: {wrongGuesses}")
    
    if livesLost == 6:
        print("You lose!")
        print(f"The word was: {activeWord}")
        print("--------------------------------------------")
        sys.exit()
    
    print("--------------------------------------------")
    
    
print("You win!")
print(f"The word was: {activeWord}")
print("--------------------------------------------")
sys.exit()