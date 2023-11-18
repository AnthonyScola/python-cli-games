#!/usr/bin/env python3
#=======================================#
#   Python Examples                     #
#   By: Anthony Scola                   #
#   Updated: 11/18/2023                 #
#                                       #
#=======================================#

import textwrap
import random

try:
  import readline
except ImportError:
  pass

from blackjack import blackjack_game

# Helpers

def clear():
  # Clear the screen
  print("\033c", end="")

def game_select(case):
  switch = {
    "1": guess_numbers,
    "2": blackjack_game
  }

  return switch.get(case, quit_game)()

def get_dificulty():
  dificulty_mode = {
    0: "\033[31m\033[1mN\033[91mo\033[93mo\033[92mb\033[94m!\033[95m!\033[96m!\033[0m",  # Rainbow-colored "Noob"
    1: "\033[92mEasy\033[0m",         # Green
    2: "\033[93mMedium\033[0m",       # Yellow
    3: "\033[91mHard\033[0m",         # Red
    4: "\033[94mImpossible\033[0m",   # Blue
    5: "\033[95mInsane\033[0m",       # Purple
    6: "\033[96mGod\033[0m",          # Cyan
    7: "\033[98mHacker\033[0m",       # Gray
  }
  clear()
  print("Choose a dificulty")
  print("1. Easy\n2. Medium\n3. Hard")
  dificulty = int(input("> "))
  while dificulty not in dificulty_mode:
    print("Please choose a valid dificulty")
    dificulty = int(input("> "))
  clear()
  print(f"[Playing on {dificulty_mode.get(dificulty)} dificulty]\n")

  return dificulty


# Games

def guess_numbers():
  dificulty = get_dificulty()
  number_range = 10**dificulty
  attempts = max(1, 10 * dificulty - 5)

  print("Now playing guess numbers\n")
  print(f"Guess a number between 1 and {number_range}")
  print(f"You have {attempts} guesses")

  secret_number = random.randint(1,number_range)

  guess = int(input("> "))
  for i in range(1,attempts+1): # Run the loop for the number of attempts Plus an extra one to check if the guess is correct
    if i == attempts:
      if guess == secret_number:
        print(f"\033cThat's right! You guessed the secret number, \033[92m{secret_number}\033[0m in {i} attempts!")
        return
      else:
        print(f"\033cYou ran out of guesses!\nThe secret number was \033[91m{secret_number}\033[0m")
        return

    if guess < secret_number:
      print("Guess higher")
      guess = int(input("> "))
    elif guess > secret_number:
      print("Guess lower")
      guess = int(input("> "))
    elif guess == secret_number:
      print(f"\033cThat's right! You guessed the secret number, \033[92m{secret_number}\033[0m in {i} attempts!")
      return

  return


def quit_game():
  print("Exiting...")
  return exit()


def main():
  clear()
  while True:
    user_input = input(textwrap.dedent("""\
      Please type the number corresponding to the game that you'd like to play. ('q' to quit)\n
      1. Guess Numbers
      2. Black Jack\n
      > """))

    game_select(user_input)


if __name__ == "__main__":
  print("Welcome to Python Games")
  main()
