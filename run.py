"""
Main run game file for 'Numberex'
"""
import sys

import random
import pyfiglet


numberex = pyfiglet.figlet_format("       Numberex", font="contessa")
print(numberex)


def user_guess(num):
    """
    Function to generate a random number between 1 and 10 for the user to guess
    """
    random_number = random.randint(1, num)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Make a guess at a number between 1 and {num}: '))
        print(guess)
        try:
            guess = int(guess)
        except IndexError():
            print(f'Sorry, {name}, that is not a number!')
        if guess < random_number:
            print(f'Sorry {name}, Guess a little higher!\n')
        elif guess > random_number:
            print(f'Sorry {name}, Guess a little lower!\n')
    print(f'Well done! You guessed the correct number {random_number}\n')
    while guess != random_number:
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
        if guess_count < guess_limit:
            guess = input("Enter Your Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True
        if out_of_guesses:
            print("Sorry, you ran out of guesses")
        else:
            print("Well done, you guessed correctly")


def computer_guess(num):
    """
    Allows user to think of a number between 1 and 10 for the AI to guess with
    higher(H) lower(L) or correct(C) options
    """
    high = num
    low = 1
    computer_feedback = ''
    guess = 0

    while True:
        # If the user selects C
        if computer_feedback == 'c':
            print(f'AI guessed {guess}, the number you were thinking of..\n')
            break

        # If the upper and lower limits do not match
        if low != high:
            # This will only be called if the user tries to cheat
            try:
                guess = random.randint(low, high)
                computer_feedback = ''
            # If the user has cheated (all the way up then all the way down)
            # Game prints a statment and breaks out of the loop
            except ValueError:
                print("I am not playing this game with you anymore!")
                break
        else:
            guess = low
            computer_feedback = ''

            # Loops indefinitely until the user selects a valid choice
        while computer_feedback not in ['c', 'l', 'h']:
            computer_feedback = input(f'         Is my number {guess} \n \
            too high(H), too low(L) or correct(C)?? \n')

        if computer_guess == 'H':
            high = guess - 1
        elif computer_guess == 'L':
            low = guess + 1


def start_game(question):   # requires some attention
    """
    Function to give the user the option to start the game
    with y/n Yes or No.
    """
    prompt = f'{question}? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return start_game(question)
    if ans == 'y':
        return True
    return False


name = input("         Enter your name: ")
print("         Hello " + name + ",  Welcome to Numberex!")

computer_guess(10)
user_guess(10)


def game_restart(game_type):
    """
    This function will restart the game if the user has come to the end,
    The function will also check if the user wishes to make a choice on which
    game to restart.
    """
    while start_game("Do you want to restart the game? "):
        if game_type == 'u':
            computer_guess(10)
        if game_type == 'c':
            user_guess(10)
        else:
            game_type("please make a choice")


print("Thank you for playing!")
sys.exit(0)
