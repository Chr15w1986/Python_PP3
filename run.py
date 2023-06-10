"""
Main run game file for 'Numberex'
"""

import random
import pyfiglet


def generate_ascii_art(text: str) -> str:
    return pyfiglet.figlet_format(text, font="contessa")


def end_game(num: int, name: str) -> None:
    restart_game = input(f"{name}, do you want to restart the game? [Y/N] ")
    while restart_game.lower() not in ["y", "n"]:
        restart_game = input(f"{name}, do you want to restart the game? [Y/N] ")

    if restart_game.lower() == "y":
        print(f"\nWelcome back, {name}!\n")
        choose_number(name)
    else:
        print("Thank you for playing Numberex!")


def play_game(num: int, name: str) -> None:
    random_number = random.randint(1, num)
    guess_count = 1
    guess_limit = 5

    while guess_count <= guess_limit:
        guess = input(f"Make a guess at a number between 1 and {num}: ")

        try:
            guess = int(guess)

            if 1 <= guess <= num:
                if guess < random_number:
                    print(f"Sorry, {name}, guess a little higher!")
                    print(f"Guesses remaining: {guess_limit - guess_count}\n")
                elif guess > random_number:
                    print(f"Sorry, {name}, guess a little lower!")
                    print(f"Guesses remaining: {guess_limit - guess_count}\n")
                else:
                    print(f"Well done! You guessed the correct number: {random_number}\n")
                    return

                guess_count += 1
            else:
                print(f"Please choose a number between 1 and {num}")
        except ValueError:
            print(f"Sorry, {name}, that is not a number!")

    print(f"Sorry, you ran out of guesses. My number was: {random_number}\n")


def computer_guess(num: int, name: str) -> None:
    low = 1
    high = num
    guess = 0
    feedback = ""

    while feedback != "c":
        if low > high:
            print(f"I think you are cheating, {name}.\nI am not playing this game with you anymore!")
            return

        guess = random.randint(low, high)
        feedback = input(f"Is your number {guess}?\nToo high (H), too low (L), or correct (C)? ")

        while feedback.lower() not in ["h", "l", "c"]:
            feedback = input(f"Is your number {guess}?\nToo high (H), too low (L), or correct (C)? ")

        if feedback.lower() == "h":
            high = guess - 1
        elif feedback.lower() == "l":
            low = guess + 1


def choose_number(name: str) -> None:
    while True:
        try:
            user_number = int(input(f"{name}, please choose an upper limit: "))
            break
        except ValueError:
            print("Please select a valid number")

    play_game(user_number, name)
    computer_guess(user_number, name)
    end_game(user_number, name)


if __name__ == "__main__":
    print(generate_ascii_art("Numberex"))

    while True:
        user_name = input("Enter your name: ").strip()
        if user_name:
            break

    print(f"\nHello {user_name}, Welcome to Numberex!\n"
          "The game rules are simple:\n"
          "- Choose your upper number limit\n"
          "- The higher the number, the harder the game!\n"
          "- You have 5 attempts to guess the number\n"
          "- Firstly, you try and guess the AI's number\n"
          "- Secondly, the AI will try and guess your number\n")

    choose_number(user_name)
