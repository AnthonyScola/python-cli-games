import textwrap
import random
from .utils import *


def print_board(active_deck, dealer_hand, player_hand, player_balance):
  clear()
  cards_left = str(len(active_deck)).rjust(2)  # Convert deck length to a two-digit number
  print(textwrap.dedent(f"""\
  ╒═════════════════[ Black Jack ]═════════════════╕
  │ Balance: ${str(player_balance).ljust(22)} {cards_left} Cards left │
  └────────────────────────────────────────────────┘\
  """))
  print(f"Dealer's hand:\n[##] [{colorize_card(dealer_hand[1])}]\n")
  print_hand(player_hand)

def resolve_game(dealer_hand, player_hand, player_balance):
  dealer_hand_value = evaluate_hand(dealer_hand)
  player_hand_value = evaluate_hand(player_hand)

  print(f"\nDealer's hand: {dealer_hand} ({dealer_hand_value})")
  print(f"Your hand: {player_hand} ({player_hand_value})")

  if player_hand_value > 21:
    print("Bust!")
    player_balance -= 100
  elif dealer_hand_value > 21:
    print("Dealer busts!")
    player_balance += 100
  elif player_hand_value > dealer_hand_value:
    print("You win!")
    player_balance += 100
  elif player_hand_value < dealer_hand_value:
    print("You lose!")
    player_balance -= 100
  else:
    print("Push!")

  print(f"Your balance: ${player_balance}")
  return player_balance

def blackjack_game():
  active_deck = standard_deck.copy()
  discard_pile = []

  dealer_hand = []
  player_hand = []

  player_balance = 1000

  player_hand_value = 0

  # Deal the cards
  for i in range(2):
    player_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))
    dealer_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))

  print_board(active_deck, dealer_hand, player_hand, player_balance)

  # Check for black jack
  if player_hand[0][0] == "A" and player_hand[1][0] == "A":
    print("Black Jack!")
    return
  
  # Player's turn
  while player_hand_value < 21:
    print("\nWould you like to (h)it or (s)tay?")
    player_input = input("> ").lower()
    if player_input == "hit" or player_input == "h":
      player_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))
      print_board(active_deck, dealer_hand, player_hand, player_balance)
      player_hand_value = evaluate_hand(player_hand)
    elif player_input == "stay" or player_input == "s":
      break
    else:
      print("Please enter a valid input")

  resolve_game(dealer_hand, player_hand, player_balance)
