"""
Main run game file for 'Numberex'
"""
import sys

import random
import pyfiglet


numberex = pyfiglet.figlet_format("       Numberex", font="contessa")
print(numberex)


def end_game(num, name):
    """
    This function will restart the game if the user has come to the end,
    The function will also check if the user wishes to make a choice on which
    game to restart.
    """
    game_restart = input("Do you want to restart the game? [Y/N]")
    while game_restart.lower() in ['y', 'n']:
        if game_restart == 'y':
            user_guess(num, name)
            computer_guess(num, name)
            game_restart = input("Do you want to restart the game? [Y/N]")
        elif game_restart.lower() == 'n':
            # if the user does not want to restart, the game ends
            print("Thank you for playing Numberex!")
            sys.exit(0)


def user_guess(num, name):
    """
    Function to generate a random number between 1 and 10 for the user to guess
    And remaining guesses (lives)
    """
    random_number = random.randint(1, num)
    guess = 0
    guess_count = 1
    guess_limit = 5
    out_of_guesses = False
    while guess != random_number and not out_of_guesses:
        guess = input(f'Make a guess at a number between 1 and {num}: ')
        # Validation to check if the input is a number
        try:
            guess = int(guess)

            if not guess > num and guess > 0:

                # User attempt loop
                if guess < random_number:
                    print(f'\nSorry {name}, Guess a little higher!')
                    print(f'Guesses remaining {guess_limit-guess_count}')
                elif guess > random_number:
                    print(f'\nSorry {name}, Guess a little lower!\n')
                    print(f'Guesses remaining {guess_limit-guess_count}')
                else:
                    print(f'Well done! You guessed the correct number \
{random_number}\n')
                # Checks how many lives are left, loops until zero
                if guess_count < guess_limit:
                    guess_count += 1
                else:
                    out_of_guesses = True
                if out_of_guesses:
                    print(f'Sorry, you ran out of guesses. \
My number was: {random_number}\n')

            else:
                print(f'Please choose a number between 1 and {num}')

        except ValueError:
            print(f'Sorry, {name}, that is not a number!')


def computer_guess(num, name):
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
            print(f'HAHA! I guessed {guess}, the number you\
 were thinking of..I WIN! ;-)\n')
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
                print(f"I think you are cheating {name}..\
I am not playing this game with you anymore!")
                break
        else:
            guess = low
            computer_feedback = ''

            # Loops indefinitely until the user selects a valid choice
        while computer_feedback not in ['c', 'l', 'h']:
            computer_feedback = input(f'         My Turn!!..Is my number {guess} \n \
            too high(H), too low(L) or correct(C)?? \n')

            # If the user states the value is too high
            if computer_feedback == 'h':
                # Validation to check if the above is possible
                # before subtracting 1
                if high > 1 and guess != 1:
                    high = guess - 1
                else:
                    print("Are you sure? ")
                    high = guess
                break

            # If the user states the value is too low
            elif computer_feedback == 'l':
                # Validation to check if the above is possible
                # before adding 1
                if low < num:
                    low = guess + 1
                else:
                    print("Are you sure? ")
                break


if __name__ == '__main__':
    # Allows the user to input their own name to play the game

    while True:
        user_name = input("         Enter your name: ").strip()
        if len(user_name) > 0:
            break
    while True:
        try:
            user_number = int(input("         Please choose an upper limit: "))
            break
        except ValueError:
            print("Please select a valid number")
    print("         Hello " + user_name + ",  Welcome to Numberex!,\n \
            * The game rules are simple,\n \
            * Firstly, you try and guess the AI number.\n \
            * Secondly, The AI will try and guess your number.\n ")

    # Called functions for main game to run
    user_guess(user_number, user_name)
    computer_guess(user_number, user_name)
    end_game(user_number, user_name)
