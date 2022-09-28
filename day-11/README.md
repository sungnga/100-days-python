# DAY 11 - The Blackjack Capstone Project


```py
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card(cards_deck):
  return random.choice(cards_deck)

def calc_score(cards):
  total = 0
  for number in cards:
    total += number
  return total

def draw_and_calculate(score, hand_cards):
  hand_cards.append(pick_card(cards))
  score = calc_score(hand_cards)
  
  for num in hand_cards:
    if score > 21 and num == 11:
      index = hand_cards.index(num)
      hand_cards[index] = 1
      score -= 10
  return {"score": score, "hand_cards": hand_cards}   
  
def loop():
  player_cards = []
  computer_cards = []
  player_score = 0
  computer_score = 0

  player_cards.append(pick_card(cards))
  player_cards.append(pick_card(cards))
  player_score = calc_score(player_cards)
  computer_cards.append(pick_card(cards))
  computer_score =calc_score(computer_cards)

  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"Computer's first card: {computer_cards[0]}")

  while player_score < 22:
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_another_card == "y":
      player_result = draw_and_calculate(player_score, player_cards)
      player_cards = player_result["hand_cards"]
      player_score = player_result["score"]
      print(f"Your cards: {player_cards}, current score: {player_score}")
      print(f"Computer's first card: {computer_cards[0]}")
    elif get_another_card == "n":
      while computer_score < 17:
        computer_result = draw_and_calculate(computer_score, computer_cards)
        computer_cards = computer_result["hand_cards"]
        computer_score = computer_result["score"]
      print(f"Your final hand: {player_cards}, final score: {player_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
      if computer_score > 21:
        print("Opponent went over. You win")
      elif player_score == computer_score:
        print("It's a draw")
      elif computer_score > player_score:
        print("You lose")
      else:
        print("You win")
      return

  while computer_score < 17:
    computer_result = draw_and_calculate(computer_score, computer_cards)
    computer_cards = computer_result["hand_cards"]
    computer_score = computer_result["score"]
  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print("You went over. You lose")

def play_blackjack():
  play = True
  while play:
    lets_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if lets_play == "y":
      clear()
      loop()
      play_blackjack()
    elif lets_play == "n":
      play = False
      
play_blackjack()
```