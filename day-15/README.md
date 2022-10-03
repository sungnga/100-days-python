# DAY 15 - Environment Setup: PyCharm

#### Today's lessons:
- Setup IDE for Python

#### Setup environment:
- Step 1: Install Python to computer. [Python](https://www.python.org/downloads/)
- Step 2: Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) and select "Community" version
- Step 3: Install PyCharm

### Day 15 project: Coffee Machine

#### Coffee Machine Program Requirements
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
  a. Check the user’s input to decide what to do next.
  b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
  a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
3. Print report.
  a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
4. Check resources sufficient?
  a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
  b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
  c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
  a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
  b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
  c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
  a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
  b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
  c. If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
7. Make Coffee.
  a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
    E.g. report before purchasing latte:
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0
    Report after purchasing latte:
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
  b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

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
	"money": 0
}


def check_payment(quarters, dimes, nickles, pennies, drink_cost):
	total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
	if total < drink_cost:
		print("Sorry that's not enough money. Money refunded.")
		return False
	else:
		change = round(total - drink_cost, 2)
		print(f"Here is ${change} in change.")
		return True


def check_resources(drink_type):
	for key in resources:
		if chosen_drink == "espresso" and key == "milk":
			continue
		if resources["key"] < drink_type["key"]:
			print(f"Sorry there is not enough {key}.")
			return False
		else:
			return True


def make_drink(drink_type, supply):
	supply["water"] -= drink_type["ingredients"]["water"]
	supply["milk"] -= drink_type["ingredients"]["milk"]
	supply["coffee"] -= drink_type["ingredients"]["coffee"]


def order_drink(drink):
	# Ask user for payment
	print("Please insert coins.")
	num_quarters = int(input("How many quarters?: "))
	num_dimes = int(input("How many dimes?: "))
	num_nickles = int(input("How many nickles?: "))
	num_pennies = int(input("How many pennies?: "))

	payment_success = check_payment(quarters=num_quarters, dimes=num_dimes, nickles=num_nickles, pennies=num_pennies, drink_cost=drink["cost"])
	resources_success = check_resources(drink)
	if payment_success and resources_success:
		make_drink(drink, resources)
		resources["money"] += drink["cost"]
		print(f"Here is your {user_input} ☕️. Enjoy!")


machine_on = True

while machine_on:
	user_input = input(" What would you like? (espresso/latte/cappuccino): ")
	chosen_drink = {}
	if user_input == "espresso":
		chosen_drink = MENU["espresso"]
	elif user_input == "latte":
		chosen_drink = MENU["latte"]
	elif user_input == "cappuccino":
		chosen_drink = MENU["cappuccino"]
	elif user_input == "off":
		machine_on = False

	if chosen_drink:
		order_drink(chosen_drink)
		print(resources)
```