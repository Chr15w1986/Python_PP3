"""
Main game file for 'Number X'
"""
import random


def guess(num):
    """
    Function to generate a random number between 1 and 10
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


guess(10)
