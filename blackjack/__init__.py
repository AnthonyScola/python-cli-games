import textwrap
import random
from .utils import *

active_deck = standard_deck.copy()
discard_pile = []

player_balance = 1000


def print_board(active_deck, dealer_hand, player_hand, show_dealer_hand=False):
  clear()
  cards_left = str(len(active_deck)).rjust(2)  # Convert deck length to a two-digit number
  print(textwrap.dedent(f"""\
  ╒═════════════════[ Black Jack ]═════════════════╕
  │ Balance: ${str(player_balance).ljust(22)} {cards_left} Cards left │
  └────────────────────────────────────────────────┘\
  """))
  
  if show_dealer_hand:
    print_hand(dealer_hand, "Dealer's hand")
  else:
    print(f"Dealer's hand:\n[##] [{colorize_card(dealer_hand[1])}]")
    print(f"Total: ??\n")

  print_hand(player_hand, "Your hand")

def resolve_game(active_deck, dealer_hand, player_hand, player_balance):
  dealer_hand_value = evaluate_hand(dealer_hand)
  player_hand_value = evaluate_hand(player_hand)
  discard_pile.extend(dealer_hand + player_hand)

  print_board(active_deck, dealer_hand, player_hand, show_dealer_hand=True)
  if player_hand_value > 21:
    print("Bust!")
    player_balance -= 100

    if player_balance <= 0:
      print("You're out of money!")
      return_to_main_menu()

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

def return_to_main_menu():
  global active_deck
  global player_balance

  print(f"\033cYour final balance: ${player_balance}\nReturning to main menu...\n\n")

  active_deck = standard_deck.copy()
  player_balance = 1000
  return

def blackjack_game():
  global player_balance

  dealer_hand = []
  player_hand = []

  player_hand_value = 0

  random.shuffle(active_deck)

  # Deal the cards
  for i in range(2):
    if len(active_deck) < 10:
      active_deck.extend(discard_pile)
      discard_pile.clear()
      random.shuffle(active_deck)

    dealer_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))
    player_hand.append(active_deck.pop(random.randint(0,len(active_deck)-1)))

  print_board(active_deck, dealer_hand, player_hand)

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
      print_board(active_deck, dealer_hand, player_hand)
      player_hand_value = evaluate_hand(player_hand)
    elif player_input == "stay" or player_input == "s":
      break
    else:
      print("Please enter a valid input")

  player_balance = resolve_game(active_deck, dealer_hand, player_hand, player_balance)

  play_again = input("Would you like to play again? (y/n) ").lower()
  if play_again == "y" or play_again == "yes":
    blackjack_game()
  else:
    return_to_main_menu()
