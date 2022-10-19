# DAY 14 - Higher Lower Game Project

- Link to the official Higher Lower Game: http://www.higherlowergame.com/
- Files: main.py, art.py, game_data.py

### Version 1
```py
import random
from replit import clear
from higher_lower_art import logo, vs
from higher_lower_game_data import data

def format_data(account):
  name = account["name"]
  description = account["description"]
  follower_count = account["follower_count"]
  country = account["country"]
  return [name, description, country, follower_count]

def compare_follower_count(acct_a, acct_b):
  if acct_a[3] > acct_b[3]:
    higher = "a"
  else:
    higher = "b"
  return higher

def game():
  account_a = format_data(random.choice(data))
  account_b = format_data(random.choice(data))
  score = 0
  continue_game = True

  print(logo)

  while continue_game:
    account_b = format_data(random.choice(data))
    while account_a == account_b:
      account_b = format_data(random.choice(data))

    print(f"Compare A: {account_a[0]}, a {account_a[1]}, from {account_a[2]}.")
    print(vs)
    print(f"Against B: {account_b[0]}, a {account_b[1]}, from {account_b[2]}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    higher = compare_follower_count(account_a, account_b)
    if guess == higher:
      score += 1
      account_a = account_b
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      continue_game = False

game()
```

### Version 2
```py
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
```
