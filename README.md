# PORTFOLIO PROJECT - 3

# NUMBEREX

## PURPOSE

'Numberex' is a number guessing game where either, You the user guesses the AI number,
or the AI tries to guess the number you are thinking of.
The project has been developed using Python programming language to create a command line app that will demonstrate the skills I have learnt.
* Here is a link to the [final project](https://numberex.herokuapp.com/)

## INITIAL IDEA CONCEPT

My initial idea for the project was to create a number guessing game to play against the computer or let the computer guess the users number.
The upper number limit can be chosen by the user for difficulty.
#  
## CONTENTS


- [USER STORIES](#user-stories)
- [FEATURES](#features)
    - []
- [TESTING](#testing)
  - [Validation](#validation)
  - [FUNCTIONALITY](#functionality)
- [TECHNOLOGIES](#technologies)
  - [DEVELOPMENT](#development)
  - [LANGUAGES USED](#languages-used) 
- [DEPLOYMENT](#deployment)
  - [REMOTE DEPLOYMENT:](#remote-deployment)
  - [HOW TO CREATE A BRANCH/TAG OF MAIN:](#how-to-create-a-branchtag-of-main)
  - [HOW TO FORK A REPOSITORY:](#how-to-fork-a-repository)
  - [HOW TO CLONE A REPOSITORY:](#how-to-clone-a-repository)
  - [HOW TO MAKE A LOCAL CLONE](#how-to-make-a-local-clone)
  - [CREDITS AND REFERENCES](#credits-and-references)
    - [IMAGE](#image)
    - [CODE](#code)
  - [ACKNOWLEDGEMENTS:](#acknowledgements)
      - [RETURN TO THE TOP](#return-to-the-top)

#

## USER STORIES

* As a user, I want the game to have varying difficulty
* As a user, I want to easily understand the main purpose of the game
* As a user, I want a choice of games
* As a user, I want to be able to see how many lives I have left
* As a user, I want the option to play again

## FEATURES

* The Features I want the game to have are:
    * Allow the user to guess a number between 1 and 10
    * To give an aspect of difficulty with 5 'lives' or attempts
    * If either game is lost or finished, the user will be presented with a restart game option

### The Game consists of:

* A terminal with the title `Numberex` and `Enter your name:`
* Once the user name has been entered, `Please choose upper limit` appears
* The user has the option to choose the highest number
* The game starts with `Make a guess between 1 and (number chosen)`
* The user makes a guess, and the game checks if it is correct
* If the user made the correct guess, they win and the turn moves to AI
* If the user makes an incorrect guess, they lose a life and must guess again
* If either, the user has run out of guesses or beat the AI, The game 
    moves to AI guesses
* The user now thinks of a number between 1 and (original number chosen)
* The AI asks the user `MY turn!! Is your number (AI Guess)`
* If the user thinks it is too high, press `h`
* If the user thinks it is too low, press `l`
* If the user thinks it is correct, press `c`
* if too high, AI guesses again
* If too low, AI guesses again
* If correct, AI shows off by telling you they won
* Option for `Do you want to restart the game [Y/N]` appears
* If the user enters `y`, Game restarts to `Make a guess between 1 and (number chosen)`
* If the user enters `n`, Game ends with `Thank you for playing Numberex!`

### Future features:

* Add AI Guesses (lives) left
* Add an option to choose between AI vs User or User vs AI
* Add how many lives the User or AI had left once correctly guessed the number


* IMAGES
    * There is one background image, for aesthetics only
    [IStockphoto](https://www.istockphoto.com/search/2/image?phrase=numbers)

* TYPOGRAPHY
    * Standard terminal font, cannot be changed.
# 

# TESTING

* `As a user, I want the game to have varying difficulty`:
    *  After the user inputs his/her name, The option to choose `highest number` will appear to
        provide a personalised level of difficulty. Outcome: `Fulfilled.`
* `As a user, I want to easily understand the main purpose of the game`:
    * Once the user has entered his/her name, and made a choice of difficulty, 
        there will be a paragraph on what the game entails. Outcome: `Fulfilled.`
* `As a user, I want a choice of games`:
    * I have provided two games that run consecutively,
        First: User to guess the AI number
        Second: Ai to guess User number. Outcome: `Fulfilled.`
* `As a user, I want to be able to see how many lives I have left`:
    * After each guess from the user, the terminal will print how many lives (guesses)
        the user has remaining, counting down from five. Outcome: `Fulfilled.`
* `As a user, I want the option to play again`:
    * I have provided an option at the end of the game that asks 
        `Do you want to restart the game? [Y/N]`
        If the user inputs `y`, the game restarts to 
        the User vs AI with the original input difficulty. 
        If the user inputs `n` the game ends with a message `Thank you for playing Numberex!`

## FLOWCHART
![Flow Chart](images/Flowchart.png)

issues:
found issue with user vs AI where the user would guess a number between 1 and 10 but if the user guessed 10, AI would say higher, or if user guessed 1 the AI would say lower.

found issue with AI vs user, where there was a double input of the user controls of H L or C, for example, if the user is thinking of 5 and AI guessed 4, I would input H for higher, but two H H would appear on seperate lines.


used pyfiglet for the title Numberex