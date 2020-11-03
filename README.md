# Welcome to Hangman!
By Sarah X, Charlie Z, Rohan N, Rivan N, and Noah p

This is a two part project. It consists of a hangman game and a number guessing game. 

To run the project, run main.py. You'll be greeted by a menu. To play hangman, input a 1. To play the guessing game, input a 2. To exit the menu, input a 0.

This project was created with equal effort for all of our team members. However, different pair shares focused on different games. Rivan and Sarah focued on Hangman, while Charlie, Rohan and Noah focused on the guessing game. 

The two games are detailed below. 

## HANGMAN GAME

This game is obtained by selecting '1' from the main menu.

This game is intended for two players. Start off the game by inputting the names of the two different players. For singleplayer, feel free to input another random name.

Next, the player 1 will input a word or phrase. This will be the word or phrase that the second player will attempt to guess.

After the player 1 has inputed a phrase, player 2, or the "guessing player" will proceed to guess letters until either they have guessed the phrase, or the man has died.

Every time an incorrect letter is guessed, another appendage is added to the hanging man. If the man is completed, he "dies" and player 1 wins.

If the "guessing player" or player 2 is able to guess the word before the man dies, player 2 wins.

At the end of the game, the program will tell you who the winning player is.

NOTE: While playing with two real people, player 2 should look away while player 1 inputs their phrase.


### What we learned while doing this project
In our hangman game, we utilize ascii art and variables in order to create the different game board statuses. After this there are while loops to keep the game running as long as it hasn't ended due to a win or loss. There are also elif statements to print the ascii art and tell whether the game has ended or not. The length of the word inputs are used as dashes that the guessed letters will appear in. There is also the use of operators like += in order to change the status of the game. 

## GUESSING GAME

This game is obtained by selecting '2' from the main menu.

Play by guessing a number between 1 and 100. The game generates a number, and the goal of the game is to guess it. Each time you guess, the game will tell you whether you guessed too high or too low.

You play until you win, and the aim of the game is to win with the lowest possible amount of guesses.

### What we learned while doing this project
Within our guessing game we were able to limit how many guesses our players were allowed and implement a guess counter. It taught usabout if statements elif statements, else statements, and redefining variables. We are also attempting to use the newly learned try function in order to check if any of the guesses were invalid. To further our learning, this game was made with us defining functions so that they could be called upon in the main menu.

## KNOWLEDGE OF FUNDAMENTALS OF PROGRAMMING


### Strings and Numbers

Within both of our games we demonstrated knowledge of strings and numbers by verifying that user inputs are valid. An example of this is in our guessing game try loop. We showcased that we knew we couldn't allow the user to input a string when guessing the magic number, so we would make the try loop make the users guess into an integer to make sure it was a number. If it was a string, then the program would have told the user they had an invalid input.

### Variables and Assignments

Through this project, we learned how to assign certain values to variables. One promininent example of this is how in our hangman game,we would assign variables certain progressions of the ASCII art in order to correctly show the progression of the man getting hung in the game. For example, we assigned empty to an empty ASCII art version of the hangman board.

### Lists and Dictionaries

By doing our hangman project, we also learned about lists and dictionaries and how to implement them into our code. An example of this is how in our main menu we have a dictionary that stores the functions that store our seperate games. To add on to this, in our menu function we decided to use our knowledge of lists to print the menu rather than just having multiple print statements.

### Iterations and Functions 

By doing our hangman project, we learned a lot about how to utilize functions and iterations. For example, in our menu, we use iterations in order to repeat the code for a certain answer. If answer 1 is chosen then the while statement will allow the code to repeat until completed. We also used functions as seen in all of the sections. Each game defines a function and the menu, utilizing iterations, will allow us to run these functions and ultimately run the entire code, making these extremely useful. 

## UPDATE LOG

This will have all of our updates on this project and what we implemented on each day. It will be a useful tool for viewers to see how far we have come as coders.

### Dates

## 10/1
We implemented a list into our menu, instead of having 3 seperate print statements for the different options the user could choose in order to make the code look nicer and more organized. 

## 9/30
We added if statements to our guessing game in order to tell whether the user guessing below or above the boundaries of 1 and 100, and if they did, a message would appear that the user's input was either below or above the boundaries. 

## 9/29
We figured out the issue of the try statement in our menu, and instead used a while loop in our guessing game along with a try and except statement within the loop in order to avoid the user's invalid inputs of numbers that weren't whole integers or inputs that were not numbers. 

## 9/25
We replaced our old menu with a new menu, involving a dictionary, try statements and except statements. However, we also found an issue with the try statements we were using. For some reason, if the user put an invalid input into the games, it would not go to that game's except statement, and instead would go to our menu's except statement.

## 9/24
We added a limit to the amount of turns allowed for the user in the guessing game by adding a 10 turn limit and using an if statement to say if the user won or lost, depending on if they reached 10 turns or not. We also added a visual counter that would tell the player how many guesses they had out of 10 after each guess.

## 9/23
We added another game into our project, which was a simple guessing game. In the game, we simply defined variables, and used if, else and elif statements to tell whether the user guessed the random number between 1 and 100 correcty, or if their guess was too low or too high. 

## 9/17
We started wondering how we would make a menu for our hangman project and what other game we should add, so that the user would have a variety of choices, rather than just hangman. We learned how to call functions in the main menu and how to define functions that would later be called upon when the user selected a certain option.

## 9/16
Up until now we have all been working on our five hour challenges and have finally completed a fully functioning hangman game. However, we are thinking of adding more that makes the game more complete, such as telling the losing user what the word is when they lose.

## 9/11
We learn that the other group is working on a calculator and other tools to assist the user. This inspired us to start thinking about a menu for our game.

## 9/8
We begin our project and have come up with many game ideas. At the moment we are leaning towards challenging ourselves in exectuing a functioning hangman game that two players can play.