def print_hand(player_hand):
  print(f"Your hand:")
  print(' '.join([f'[{colorize_card(card)}]' for card in player_hand]))
  print(f"Total: {evaluate_hand(player_hand)}")

def clear():
  # Clear the screen
  print("\033c", end="")

def colorize_card(card):
  if card[-1] == "♠" or card[-1] == "♣":
    return f"\033[90m{card}\033[0m"
  elif card[-1] == "♡" or card[-1] == "♢":
    return f"\033[91m{card}\033[0m"

standard_deck = [
  "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
  "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
  "A♡","2♡","3♡","4♡","5♡","6♡","7♡","8♡","9♡","10♡","J♡","Q♡","K♡",
  "A♢","2♢","3♢","4♢","5♢","6♢","7♢","8♢","9♢","10♢","J♢","Q♢","K♢"
  ]

def evaluate_hand(hand):
  hand_value = 0
  aces = 0
  for card in hand:
    if card[0] == "A":
      hand_value += 11
      aces += 1
    elif card[0] in ["J", "Q", "K"]:
      hand_value += 10
    else:
      hand_value += int(card[:-1])
  while hand_value > 21 and aces:
    hand_value -= 10
    aces -= 1
  return hand_value