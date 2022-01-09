"""
Main run game file for 'Numberex'
"""
import random
import pyfiglet


numberex = pyfiglet.figlet_format("       Numberex", font="contessa")
print(numberex)


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
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        computer_feedback = input(f'         Is my number {guess} \n \
        too high(H), too low(L) or correct(C)?? \n')
        print(computer_feedback)
        if computer_guess == 'H':
            high = guess - 1
        elif computer_guess == 'L':
            low = guess + 1

    print(f'AI guessed {guess}, the number you were thinking of..\n')


# name input function
name = input("Enter your name: ")
print("Hello " + name + ", Welcome to Numberex!")

# start game with choice of user vs AI or AI vs user.


computer_guess(10)
guess(10)
