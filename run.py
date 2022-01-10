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
            print(f'Sorry {name}, Guess a little higher!\n')
        elif guess > random_number:
            print(f'Sorry {name}, Guess a little lower!\n')

    print(f'Well done! You guessed the correct number {random_number}\n')


def computer_guess(num):   # requires some attention
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
        if computer_guess == 'H':
            high = guess - 1
        elif computer_guess == 'L':
            low = guess + 1

    print(f'AI guessed {guess}, the number you were thinking of..\n')


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
print("         Hello " + name + ", Welcome to Numberex!")

computer_guess(10)
guess(10)

exit()
