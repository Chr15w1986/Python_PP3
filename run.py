"""
Main game file for 'Number X'
"""
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Make a guess at a number between 1 and {x}: '))
        print(guess)


guess(10)
