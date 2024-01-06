import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) 
        self.word_guessed = ["_"] * len(self.word) # List to track the letters guessed so far
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]
        
    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the chosen word.
        Prints a message indicating whether the guess is correct.
        """
        
        guess = guess.lower()
        correct_guess = False
        
        if guess in self.word:  
            for i, letter in enumerate(self.word):
                if letter == guess and self.word_guessed[i] == '_' :
                    self.word_guessed[i] = guess 
                    correct_guess = True # set correct_guess condution to determine to win or lose
        
            if  correct_guess: 
                print(f"Good guess! {guess} is in the word.")
                self.num_letters -=1
            
        else :
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")  
                  
    def ask_for_input(self):
        """
        Continuously prompts the user to enter a single letter.
        Calls check_guess function to verify the guess.
        Exits the loop if a valid letter is guessed.Continues prompting until the game is won or the player runs out of lives.
        """
        while True:
            guess = input("Please enter a single letter: ")
            if not guess.isalpha() and len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print( "You already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                
                # Check for win or lose conditions                          
                if self.num_lives <= 0:
                    print("Game over! Please try again!")                    
                    break                        
                
                elif "_" not in self.word_guessed: 
                    print(f"Congratulations! You've guessed the word: {self.word}")
                    break        
                      
word_list = ["apple", "banana", "cherry"]
game = Hangman(word_list)
game.ask_for_input()