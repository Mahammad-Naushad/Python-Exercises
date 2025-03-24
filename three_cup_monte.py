"""
This program is written for three cup monte game.
You will have three cups and a ball inside one cup. User has to guess which cup has the ball inside it
"""
from random import  shuffle


def shuffle_list(my_list):
    shuffle(my_list)


def player_guess():
    guess = ""

    while True:
        if guess not in ["0", "1", "2"]:
            guess = input("Enter your guess(0,1 or 2): ")
        else:
            return int(guess)


def check_guess(my_list, guess):
    return my_list[guess] == "ball"


three_cup_list = ["", "ball", ""]
shuffle_list(three_cup_list)
guess_index = player_guess()

if check_guess(three_cup_list, guess_index):
    print(f"You guessed it right! \nCorrect position is {three_cup_list}")
else:
    print(f"Wrong guess! \nCorrect position is {three_cup_list}")
