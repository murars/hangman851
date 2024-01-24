# **Hangman Game**

Hangman is a classic game where one player thinks of a word, and another tries to guess it within a certain number of attempts. 

This project is a digital implementation of the Hangman game, where the computer selects a word and the user attempts to guess it.

## **Stage I: Installations and Creating a Virtual Environment**

**1 - Install Visual Studio Code (VS Code):**
- Download and install VS Code, the environment where the code will be written.

**2 - Setup the Project Environment:**
- Open a terminal in VS Code.
- Create a project directory:
```
mkdir AICorePytEnv
```
- Install Miniconda3, a smaller version of Anaconda covering essential Python packages.
- Create and activate a virtual environment:
```
conda create --name AIcorePytEnv_env
conda activate AIcorePytEnv_env 
```

**3 - Install Git and GitHub:**
- Set up Git for version control.
- Use GitHub to create a repository and copy the remote hangman851 repository into your local environment.
- 
**Learnings:** 
- How a virtual environment is created and understanding the importance of a virtual environment. 
- Understanding the version control with Git.


## **Stage II: Clone the Remote Repository**

**1 - Clone the Repository:**

- Use the command in your terminal:
```
git clone https://github.com/your-repository/hangman.git
```
- This clones the game files to your local machine.

**2- Navigate to the Game Directory:** 
- Your directory structure should look like this:
```
-hangman851
 --hangman
   -hangman_Template.py
```

**Learnings:**
- Gained a deeper understanding of the significance of using remote repositories on GitHub for collaborative projects. Learned how efficient and essential it is to share code and track changes in a team environment, enhancing the overall workflow and ensuring version control.


## **Stage III: Coding the Game**

**1 - Create milestone_2.py:**
```
touch milestone_2.py
```
- This file requires knowledge of random(), input(), len(), isalpha() functions, and if-else statements.
- Implement features like word selection, user input handling, and basic validation.

**Learnings:**
- Python Programming Foundations: This project deepened my understanding of Python programming fundamentals. By implementing the Hangman game, I became more familiar with the syntax and core concepts of the language, which are crucial for any Python developer.

- Utilizing Python Functions:
  - random(): I learned how to use the random library to randomly select words from a list. This was a key part of the game logic, as it simulates the unpredictability of an opponent in the traditional Hangman game.
  - input(): Implementing the input() function allowed me to understand how to interact with users in a console application. I gained experience in receiving and processing user input, which is a fundamental aspect of interactive programs.
- Control Structures:
  - If-Else Statements: The use of if-else statements was pivotal in determining the game's flow, especially in handling correct and incorrect guesses. I learned how to use these statements to control the game's logic, such as updating the number of lives remaining and revealing the correctly guessed letters.
  - Loop Control: Implementing the game loop using while demonstrated how to repeatedly prompt the user for input until the game ends, either by guessing the word correctly or running out of lives. This helped me grasp the concept of loop control and its application in maintaining the game's active state.


**2 - Create milestone_3.py:**
```
touch milestone_3.py
```

**Learnings:**
- Loop Control and Continuity: Developing milestone_3.py taught me the essentials of loop control in Python, particularly using while True to create a continuous game loop. This was crucial for maintaining the game until the player either guesses the word or runs out of lives.
- User Input Validation: I learned how to validate user input more effectively. Ensuring that the input is a single letter and handling unexpected inputs were key aspects of creating a robust and user-friendly game.
- Case-Insensitive Comparison: Implementing .lower() to convert user input into lowercase was a simple yet significant learning point. It highlighted the importance of case-insensitive comparison in applications where user input can vary in case.


**3 - Create milestone_4.py:**
```
touch milestone_4.py
``````

**Learnings:**
- Object-Oriented Programming (OOP): In milestone_4.py, I delved into OOP in Python. Creating a Hangman class helped me understand how to encapsulate game logic and attributes within a class structure.
- Classes and Methods: Learning to define methods within a class and using class instances was transformative. It made the code more organized, modular, and reusable, which are critical aspects of effective software development.
- Structural Advantages: I recognized the advantages of structuring a program using classes and objects. It facilitated better organization of code, made it more readable, and allowed for easier debugging and future enhancements.

**4 - Create milestone_5.py:**
```
touch milestone_5.py
```
- Implement the main game loop and ensure it runs correctly under if __name__ == '__main__':

**Learnings:**
- Integration of Game Components: In milestone_5.py, my focus was on integrating the various components of the game. This process taught me how different parts of a program interact and work together to create a cohesive application.
- Significance of if __name__ == '__main__':: Understanding this Python idiom was crucial. It allowed me to design the script to be run as a standalone program or imported as a module without executing the game immediately. This is a best practice in Python programming for structuring scripts effectively.
- Bringing the Project Together: Finalizing the game involved not only code integration but also a thorough testing phase. I learned the importance of testing and debugging to ensure the game runs smoothly and provides a good user experience.
