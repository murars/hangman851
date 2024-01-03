
import random

fruit_list = ["watermelon","pomegranate", "banana", "apple", "melon"]
print(fruit_list)

chosen_fruit = random.choice(fruit_list)
print(chosen_fruit)

def check_guess(guess, chosen_fruit):
   
    guess=guess.lower()

    if  guess in chosen_fruit:
        print( f"Good guess! {guess} is in the word.")
    else:
        print( f"Sorry, {guess} is not in the word. Try again.")
        
def ask_for_input(chosen_fruit):
    
   while True:
    guess = input("Please enter a single letter: ")
    if guess.isalpha() and len(guess)==1:
        check_guess(guess, chosen_fruit) 
        break
    else :
        print( "Invalid letter. Please, enter a single alphabetical character.")  

ask_for_input(chosen_fruit)