#Hangman game
#----imports----
import random

#------constants-----

Hangman =(    
    """
    -------
    |      |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    0
    |
    |
    |
    ----------
    """,
    """
    -------
    |     |
    |     0
    |    -+-
    |
    |
    ----------
    """,
    """
    -------
    |     |
    |     0
    |   /-+-
    |
    |
    ----------
    """,
    """
    -------
    |     |
    |     0
    |   /-+-/
    |
    |
    ----------
    """,
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     |
    |
    ----------
    """,
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     |
    |    / 
    ----------
    """,
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     |
    |    / \
    
    ----------
    """)

MAX_WRONG = len(Hangman)-1
words = ("GEWGAW", "TAFETTA","CLAM", "PHILTER","AGITPROP")

#---INITIALIZING VARIABLES---
word = random.choice(words)     #choice is from the random module
so_far = "-" *len(word)
wrong = 0     #this is a type of sentry variable (look it up)
used = []

print("Welcome to Hangman!")
while wrong < MAX_WRONG and so_far != word:
    print(Hangman[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far the word is: \n", so_far)
    guess = input("Enter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("you already guessed the letter", guess)
        guess = input("Enter your guess")
        guess = guess.upper()
        
    used.append(guess)
    
    
    if guess in word:
        print("\nYes!", guess, "is in word")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry ", guess, "isn't in the word")
        wrong += 1
        
if wrong == MAX_WRONG:
    print(Hangman[-1])
    print("you've been hanged")
    print("the word was", word)
else:
    print("you guessed it!")
    print("the word was", word)
    
          
