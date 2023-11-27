import math
import textwrap
import random
import time
from .utils import *

player_bets = []
player_balance = 1000

def print_board(winning_number):
  random_offset = random.randint(0,36) # Offset to mask the winning number
  iRange = 148-random_offset # subtract offset to sync board with ball position
  offset_winning_number = winning_number + random_offset % 37 # add back offset to preserve winning number
  slowdown_factor = [0.005 * math.exp(i/50) for i in range(iRange)] #friction
  balance_string = f"Balance: ${str(player_balance).ljust(22)}"
  roulette_hud = textwrap.dedent(f"""\
  ╒══════════════════[ Roulette ]══════════════════╕ \033[?25l
  │ {balance_string}               │
  └────────────────────────────────────────────────┘\
  """)
  for i in range(iRange):
    clear()
    ball_pos = (4*(i+(offset_winning_number)+1)+1) % 148
    print(roulette_hud + '\n' + ' '*ball_pos + "\033[97m●\033[0m" + '\n' + roulette_board_string)
    time.sleep(slowdown_factor[i])
  print(f"The winning number is {winning_number}!\033[?25h")

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
