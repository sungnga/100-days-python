# DAY 15 - Environment Setup: PyCharm

### Today's lessons:
- Setup IDE for Python

### Setup environment:
- Step 1: Install Python to computer. [Python](https://www.python.org/downloads/)
- Step 2: Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) and select "Community" version
- Step 3: Install PyCharm

### Day 15 project: Coffee Machine

#### Coffee Machine Program Requirements

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”\n
   a. Check the user’s input to decide what to do next.\n
   b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.\n
   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
3. Print report.\n
   a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.\n
   Water: 100ml\n
   Milk: 50ml\n
   Coffee: 76g\n
   Money: $2.5
4. Check resources sufficient?\n
   a. When the user chooses a drink, the program should check if there are enough resources to make that drink.\n
   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”\n
   c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.\n
   a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.\n
   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01\n
   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?\n
   a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.\n
   b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.\n
   Water: 100ml\n
   Milk: 50ml\n
   Coffee: 76g\n
   Money: $2.5\n
   c. If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
7. Make Coffee.\n
   a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.\n
   E.g. report before purchasing latte:\n
   Water: 300ml\n
   Milk: 200ml\n
   Coffee: 100g\n
   Money: $0\n
   Report after purchasing latte:\n
   Water: 100ml\n
   Milk: 50ml\n
   Coffee: 76g\n
   Money: $2.5\n
   b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

### Coffee Machine v1
```py
MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
  }

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
  }
profit = 0


def is_resource_sufficient(drink_name):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in resources:
    if drink_name == "espresso" and item == "milk":
      continue
    if resources[item] < MENU[drink_name]["ingredients"][item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True


def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  num_quarters = int(input("How many quarters?: "))
  num_dimes = int(input("How many dimes?: "))
  num_nickles = int(input("How many nickles?: "))
  num_pennies = int(input("How many pennies?: "))

  total = (num_quarters * .25) + (num_dimes * .10) + (num_nickles * .05) + (num_pennies * .01)
  return total


def is_transaction_successful(payment, drink_cost):
  """Returns True when the payment is accepted, False if money is insufficient."""
  if payment < drink_cost:
    print("Sorry that's not enough money. Money refunded.")
    return False
  else:
    change = round(payment - drink_cost, 2)
    print(f"Here is ${change} in change.")
    return True


def make_coffee(drink_name):
  """Deduct the required ingredients from the resources."""
  resources["water"] -= MENU[drink_name]["ingredients"]["water"]
  resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]
  if not drink_name == "espresso":
    resources["milk"] -= MENU[drink_name]["ingredients"]["milk"]


machine_on = True
while machine_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")

  if choice in MENU:
    if is_resource_sufficient(choice):
      total_payment = process_coins()
      if is_transaction_successful(total_payment, MENU[choice]["cost"]):
        make_coffee(choice)
        profit += MENU[choice]["cost"]
        print(f"Here is your {choice} ☕️. Enjoy!")
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  elif choice == "off":
    machine_on = False
  else:
    print("Invalid input. Please try again.")
```

### Coffee Machine v2
```py
MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}
profit = 0


def is_resource_sufficient(drink_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in drink_ingredients:
    if resources[item] < drink_ingredients[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True


def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  num_quarters = int(input("How many quarters?: "))
  num_dimes = int(input("How many dimes?: "))
  num_nickles = int(input("How many nickles?: "))
  num_pennies = int(input("How many pennies?: "))

  total = (num_quarters * .25) + (num_dimes * .10) + (num_nickles * .05) + (num_pennies * .01)
  return total


def is_transaction_successful(money_received, drink_cost):
  """Returns True when the payment is accepted, False if money is insufficient."""
  if money_received < drink_cost:
    print("Sorry that's not enough money. Money refunded.")
    return False
  else:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    return True


def make_coffee(drink_name, drink_ingredients):
  """Deduct the required ingredients from the resources."""
  for item in drink_ingredients:
    resources[item] -= drink_ingredients[item]
  print(f"Here is your {drink_name} ☕️. Enjoy!")


machine_on = True
while machine_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")

  if choice in MENU:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
      total_payment = process_coins()
      if is_transaction_successful(total_payment, drink["cost"]):
        make_coffee(choice, drink["ingredients"])
        profit += drink["cost"]
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  elif choice == "off":
    machine_on = False
  else:
    print("Invalid input. Please try again.")
```
