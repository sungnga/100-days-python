import random
from replit import clear
from art import logo, vs
from game_data import data

def compare_follower_count(acct_a, acct_b):
  if acct_a["follower_count"] > acct_b["follower_count"]:
    higher = "a"
  else:
    higher = "b"
  return higher

def game():
  account_a = data[random.choice(range(len(data)))]
  account_b = data[random.choice(range(len(data)))]
  
  score = 0
  continue_game = True
  print(logo)

  while continue_game:
    account_a = account_b
    account_b = data[random.choice(range(len(data)))]
    while account_a == account_b:
      account_b = data[random.choice(range(len(data)))]

    higher = compare_follower_count(account_a, account_b)
    
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if not (guess == "a" or guess == "b"):
      guess = input("Invalid input. Must type 'A' or 'B': ").lower()

    clear()
    if guess == higher:
      score += 1
      print(logo)
      print(f"You're right! Current score: {score}.")
    else:
      continue_game = False
      print(f"Sorry, that's wrong. Final score: {score}")
      
game()