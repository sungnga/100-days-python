## Day 4 - Randomization and Lists

#### Today's lessons:
- Randomization
- Error handling
- Module
- List

#### Functions:
- .split()

#### Random module
- The Python team has built the random module for us to use because generating random numbers a frequent task in programming. We need to import the module in order to use it
  - `import random`
- Example:
  ```py
  import random

  # random whole number btwn 1 and 10, inclusively
  random_int = random.randint(1, 10)
  # random float number btwn .0000.. to 4.9999.. 
  random_float = random.random() * 5

  print(random_float)
  ```

#### Our own module
- A module is a piece of code that performs a specific functionality. A module can be used many times through out an application
- To use a module, simply import it into the file we want to use it using the `import` keyword

#### Lists
- A list is a data structure. A data structure is a way of storing data in Python
- A list starts with square brackets `[item1, item2]` and the elements it holds
- The elements in a list is indexed. To access an element, simply add a pair of square bracket next to the name of the list and reference the element's index number
  ```py
  fruits = ["apple", "kiwi", "mango", "pineapple"]
  fruits[0] #apple
  ```
- Can have a positive or negative indices
  - `[0]` first item in the list
  - `[-1]` last item in the list
- To alter an item in a list, reference the item by its index number and assign a new data
  - `fruits[1] = "cherry"` -> `fruits = ["apple", "cherry", "mango", "pineapple"]`
- The `.append()` method adds an item to the end of a list
  - `fruits.append("peach")` => `fruits = ["apple", "cherry", "mango", "pineapple", "peach"]`

#### Exercise: Who's Paying
```py
import random

names = input("Give me everybody's names, separated by a comma. ")
names_list = names.split(", ")
random_choice = random.randint(0, len(names_list) - 1)
print(names_list[random_choice] + " is going to buy the meal today.")
```

#### IndexErrors, working with nested lists
- IndexError occurs because list index is out of range. This is a common error when we try to access the last item on a list by its index and forgot to subtract 1. Remember, the index position starts at 0
- To access items in a nested list, chain on square brackets `list_name[index][index]`
  ```py
  fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
  vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

  dirty_dozen = [fruits, vegetables]

  print(dirty_dozen[1][1]) # "Kale"
  ```

#### Exercise: Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")

### Day 4 project: Rock Paper Scissors
```py
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("You've typed an invalid number, you lose!")
else:
  print(game_images[user_choice])

  computer = random.randint(0, 2)
  print(f"Computer chose: {computer}")
  print(game_images[computer])

  if user_choice == computer:
    Print("It's a tie")
  elif (user_choice == 0 and computer == 1) or (user_choice == 1 and computer == 2) or (user_choice == 2 and computer == 0):
    print("You lose")
  elif (user_choice == 0 and computer == 2) or (user_choice == 1 and computer == 0) or (user_choice == 2 and computer == 1):
    print("You win")
```