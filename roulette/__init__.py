import math
import textwrap
import random
import time
from .utils import *

player_bets = []
player_balance = 1000

def print_board(winning_number):
  random_offset = random.randint(0,36) # Add a random offset so that the player does't know where the ball will land
  iRange = 185-random_offset # subtract offset from 185 so that the ball will land on the winning number
  offset_winning_number = winning_number + random_offset % 37
  for i in range(0,iRange): 
    ball_pos = (5*(i+(offset_winning_number)+1)+2) % 185  # Move 5 spaces at a time, wrap around at 37
    print(textwrap.dedent(f"""\
    \033c
    ╒══════════════════[ Roulette ]══════════════════╕
    │ Balance: ${str(player_balance).ljust(22)}               │
    └────────────────────────────────────────────────┘
    {' '*ball_pos}\033[97m●\033[0m
    {roulette_board_string}\
    """))
    time.sleep(0.005 * math.exp(i/50))  # Gradually slow down as i increases
  print(f"The winning number is {winning_number}!")

def resolve_game(winning_number, player_bets):
  player_bet_value = evaluate_bets(player_hand)

  print_board(winning_number)
  if player_bet_value > 0:
    print("You win!")
    player_balance += player_bet_value
  elif player_bet_value < 0:
    print("You lose!")
    player_balance += player_bet_value

  print(f"Your balance: ${player_balance}")
  return player_balance

def return_to_main_menu():
  global player_balance

  print(f"\033cYour final balance: ${player_balance}\nReturning to main menu...\n\n")

  player_balance = 1000
  return

def roulette_game():
  global player_balance

  player_bets = []
  player_hand_value = 0

  winning_number = random.randint(0,36)
  time.sleep(2)

  print_board(winning_number)


  # Player's turn
  while player_balance > 0:
    print("\nWould you like to place a bet?")
    player_input = input("> ").lower()
    if player_input == "hit" or player_input == "h":
      print_board(winning_number)
    elif player_input == "stay" or player_input == "s":
      break
    else:
      print("Please enter a valid input")

  player_balance = resolve_game()

  play_again = input("Would you like to play again? (y/n) ").lower()
  if play_again == "y" or play_again == "yes":
    roulette_game()
  else:
    return_to_main_menu()
