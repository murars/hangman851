
import random

## List of possible words for the Hangman game
word_list = ["watermelon","pomegranate", "banana", "apple", "melon"]
print(word_list)

# Randomly select a word from the list as the target word for the game
chosen_fruit = random.choice(word_list)
print(chosen_fruit)


def check_guess(guess,chosen_fruit):
    """
    Checks if the guessed letter is in the chosen word.
    Prints a message indicating whether the guess is correct.
    """
    guess=guess.lower()

    if  guess in chosen_fruit:
        print( f"Good guess! {guess} is in the word.")
    else:
        print( f"Sorry, {guess} is not in the word. Try again.")
            
def ask_for_input(chosen_fruit):
    """
    Continuously asks the user to enter a single letter.
    Calls check_guess function to verify the guess.
    Exits the loop if a valid letter is guessed.
    """
    while True:
        guess = input("Please enter a single letter: ")
        if guess.isalpha() and len(guess)==1:
            check_guess(guess, chosen_fruit) 
            break
    else :
        print( "Invalid letter. Please, enter a single alphabetical character.")  

ask_for_input(chosen_fruit) 