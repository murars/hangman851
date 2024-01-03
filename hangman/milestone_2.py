import random
fruit_list = ["watermelon","pomegranate", "banana", "apple", "melon"]
print(fruit_list)

chosen_fruit = random.choice(fruit_list)
print(chosen_fruit)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha(): 
    print("Good guess!")
else:   
    print("Oops! That is not a valid input")
