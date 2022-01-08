"""
Main game file for 'Number X'
"""
import random


def guess(num):
    """
    Function to generate a random number between 1 and 10 for the user to guess
    """
    random_number = random.randint(1, num)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Make a guess at a number between 1 and {num}: '))
        print(guess)
        if guess < random_number:
            print('Oops, Guess a little higher!\n')
        elif guess > random_number:
            print('Hmmm, Guess a little lower!\n')

    print(f'Well done! You guessed the correct number {random_number}\n')


def computer_guess(num):
    """
    Allows user to think of a number between 1 and 10 for the AI to guess with
    higher(H) lower(L) or correct(C) options
    """
    high = num
    low = 1
    computer_feedback = ''
    while computer_feedback != 'c':
        guess = random.randint(low, high)
        computer_feedback = input(f'Is my number {guess} too high (H), \
            too low (L) or correct(C)?? ')
        print(computer_feedback)
        if computer_guess == 'H':
            high = guess - 1
        elif computer_guess == 'L':
            low = guess + 1

    print(f'Well done! You guessed the number I was thinking of {guess}..\n')     

# name input function


# start game with choice of user vs AI or AI vs user.

guess(10)
