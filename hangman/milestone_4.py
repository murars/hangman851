import random

class Hangman:
  
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_letters = []
        print(f"The chosen word has {len(self.word)} characters")
        print(" ".join(self.word_guessed))

    def check_letter(self, letter) -> None: # -> None is a part of the function's type hinting in Python, indicating that the function does not have a return value.
        """
        Checks if the guessed letter is in the chosen word.
        Prints a message shows if the guess is correct.
        """
        letter = letter.lower()
        if letter in self.word:
            if letter not in self.list_of_letters:
                self.num_letters -= 1
            for i, current_letter in enumerate(self.word): # index yaratmak icin kullandik.
                if current_letter == letter:
                    self.word_guessed[i] = letter
            print(" ".join(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_letter(self):
        """
        Continuously asks the user to enter a single letter.
        Calls check_guess function to verify the guess.
        Exits the loop if a valid letter is guessed.
        Continues ask until the game is won or the player has no lives.
        """
        while True:
            letter = input("Please enter a single letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter just one digit character")
                
            elif letter in self.list_of_letters:
                print(f"{letter} was already tried.")
            
            else:
                self.list_of_letters.append(letter)
                self.check_letter(letter)
                break

