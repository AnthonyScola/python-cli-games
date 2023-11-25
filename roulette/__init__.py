import textwrap
import random
from .utils import *

player_bets = []
player_balance = 1000


def print_board():
  clear()
  print(textwrap.dedent(f"""\
  ╒══════════════════[ Roulette ]══════════════════╕
  │ Balance: ${str(player_balance).ljust(22)}               │
  └────────────────────────────────────────────────┘\
  """))
  

def resolve_game(active_deck, dealer_hand, player_hand, player_balance):
  player_bet_value = evaluate_bets(player_hand)

  print_board(active_deck, dealer_hand, player_hand, show_dealer_hand=True)
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

  print_board()


  # Player's turn
  while player_balance > 0:
    print("\nWould you like to place a bet?")
    player_input = input("> ").lower()
    if player_input == "hit" or player_input == "h":
      player_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))
      print_board(active_deck, dealer_hand, player_hand)
      player_hand_value = evaluate_hand(player_hand)
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
