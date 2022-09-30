# DAY 12 - Scope

#### Today's lessons:
- Namespaces
- Local vs global scope

#### Functions:
- randint() - choosing random integer between a range
  ```py
  from random import randint

  chosen_num = randint(1, 100) #random int between 1 and 100, including 100
  ```

#### Links:
- Get your own ASCII text: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

#### Namespaces: local vs global scope
- The concept of **scope** is what you have access to or what is available to you. The analogy is an apple tree that is inside a fence or outside a fence. If it's inside the fence, only people who live in the house can access it. If the tree is outside the fence, the public can access it 
- **Local scope:** 
  - Local scope exists within functions
  - When a new variable or function is created inside another function, they are only accessible within the function. They are scoped to the function and are not accessible outside of the function
  ```py
  def drink_potion():
    potion_strength = 2
    print(potion_strength) #This print function has access to potion_strength
  drink_potion()
  print(potion_strength) #Error - this print function doesn't have access to potion_strength
  ```
- **Global scope:**
  - Global scope exists at the top level of the file
  - Global variables and functions are made available anywhere, inside or outside other functions

- **Local vs global scope:**
  - The only difference between local and global scope is where you define your variables or functions
- **Namespace:**
  - Anything that you give a name to has a namespace and that namespace is valid in certain scopes. The concept of scope applies to anything you name
  - Example:
    ```py
    player_health = 10  #has global scope. Not defined inside a function

    def game():
      def drink_potion(): #has local scope to game function
        potion_strength = 2 #local scope to drink_potion function
        print(player_health) #this is valid because player_health has global scope

      drink_potion() #can only call within game function
    
    print(player_health) #this is valid
    ```
  - Where you give ***name*** to a variable or function for the first time defines the ***scope*** of that particular variable or function

#### How to modify a global variable
- We cannot modify something that is global within a local scope, unless we are explicit that we want to do so
- There is a reason why it is so difficult to modify something that has global scope and you don't want to do this very often because it's prone to creating bugs and errors. You can read it and use it within local scope, i.e. inside a function
- **Option 1 to modify a global variable:**
  - Use the `global` keyword to reference the global variable
    ```py
    enemies = 1

    def increase_enemies():
      global enemies #Modifying global variable. Use this with caution!
      enemies += 1
      print(f"enemies inside function: {enemies}") #enemies is 2
    
    increase_enemies()
    print(f"enemies outside function: {enemies}") #enemies is 1
    ```
- **Option 2 to modify a global variable:**
  - Instead of modifying the global variable within local scope in a function, we can simply `return` the global as an output. So when we call the function, we can save the output to a variable
    ```py
    enemies = 1

    def increase_enemies():
      print(f"enemies inside function: {enemies}") #enemies is 1
      return enemies += 1
    
    enemies = increase_enemies()
    print(f"enemies outside function: {enemies}") #enemies is 2
    ```
#### Python constants and global scope
- Global constants are which you define and you're never planning on changing it again
- To differentiate these global constants from global variables which you are likely to change, the naming convention in Python is to turn it into all uppercase. The uppercase also serves as a reminder to not modify its value
  - `PI = 3.14159`
  - `URL = "https://www.google.com"`
  - `TWITTER_HANDLE = @_ngala`

### Day 12 project: The Number Guessing Game
- File: art.py
- File: main.py
```py
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
# import random
from random import randint 

print(logo)
# chosen_num = random.choice(range(1, 101))
chosen_num = randint(1, 100) #random int between 1 and 100, including 100
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Psssst, the correct answer is {chosen_num}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "hard":
  attempts = 5
else:
  attempts = 10

while attempts > 0:
  print(f"You have {attempts} remaining to guess the number.")
  guess = int(input("Make a guess: "))
  
  if guess < chosen_num:
    print("Too low.")
    attempts -= 1
  elif guess > chosen_num:
    print("Too high.")
    attempts -= 1
  else:
    print(f"You've guessed the correct number, congratulations!")
    break
    
  if attempts > 0:
    print("Guess again.")
else:
  print("You've run out of guesses, you lose.")
```