Hangman is a game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

STAGE - I - Installations and creating a virtual environment. 

Install VS Code, which is the environment code that will be written.
Open a terminal in VS Code. 
Create a directory called 'AICorePytEnv' 
  * mkdir 'AICorePytEnv'
Install miniconda3 which is a small bootstrap version of Anaconda which covers the most useful Python packages. 
Create a virtual environment and activate it. 
  * conda create --name AIcorePytEnv_env
  * conda activate AIcorePytEnv_env ( you have to see virtual environment name instead of base )
Install Git for version control.
Install GitHub to create a repository and copy the remote hangman851 repository into the local.


STAGE - II - Clone the Remote Repository into the local:

Open your terminal in VS Code
Use the command: git clone https://github.com/your-repository/hangman.git
This will clone the game files to your local machine from the remote repo.
Navigate to the Game Directory: you will see;
  -hangman851
  --hangman
    -hangman_Template.py


STAGE -III - Coding the game

Change your current working directory to the game folder: cd hangman851/hangman
Following hangman_Template.py,
respectively;

Create 'milestone_2.py'  
  * in terminal 'touch milestone_2.py'
  * in this file ( milestone_2 )
    * This file's pre-requests are the knowledge of random(), input(), len(), isalpha() functions and if-else statements.
    * import 'random' package which is used to choose a word by the system.   
    * Create a 'word_list' from which the system chooses a word. The list contains "watermelon", "pomegranate", "banana", "apple", "melon"
    * Use the 'random' function which creates a word,
    * Create an 'input' function which allows the user to guess the word by inputting a letter,
    * Sets an if-else statement which consists of "len" and "isalpha" functions which respectively, check if the letter is single and alphabetic.

 Create 'milestone_3.py'
   * in terminal 'touch milestone_3.py'
   * This file's pre-requests are the knowledge of the creation of a function, .lower(), while True: statement
   * Transform the letter chosen by the user into a lowercase using the .lower() function.
   * Check the letter if there is this letter in the chosen word.
   * By while True, create a loop and continuously prompt the user to enter a single letter. Calls check_guess function to verify the guess. Exits the loop if a valid letter is guessed.  

 Create 'milestone_4.py'
   * in terminal 'touch milestone_4.py'
   * This file's pre-requests are the knowledge of the creation of a Class, Class instances, Class parameters, " ".join(), .append(), break ( exit the loop in a certain condition ), enumerate()
   * Create a Class called Hangman and define class instances which can be called later to be able to be used for different Hangman games.
   * Copy the functions from milestone_3.py refining functions name to be able to be understood easily and correctly.

Create 'milestone_5.py' 
  * in terminal 'touch milestone_4.py' 
  * This file's pre-requests are the knowledge of calling the class from out of the class, __name__ == '__main__': 
  * Create a game (function) out of the class.
  * Run the code under the same directory with the code ( __name__ == '__main__':)

