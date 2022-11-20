# Day 3 - Control Flow and Logical Operations

### Today's lessons:
- Conditionals if/elif/else
- Conditional operators
- Logical operators
- Code blocks
- Scope

### Functions:
- if/else
- if/elif/else

### Control flow with if/else and conditional operator
- if/else statement
  ```py
  if condition:
    do this
  else:
    do this
  ```
- Comparison operators
  - Greater than: `>`
  - Less than: `<`
  - Greater than or equal to: `>=`
  - Less than or equal to: `<=`
  - Equal to: `==`
  - Not equal to: `!=`
- One equal `=` means **_assignment_**
- Two equals `==` means **_check equality_**
- Modulo operation: `%`
  - The result is the remainder of the division
  - `7 % 2` -> `1`
- Exercise: Odd or Even
  ```py
  number = int(input("Which number do you want to check? "))

  if number % 2 == 1:
    print("This is an odd number.")
  else:
    print("This is an even number.")
  ```

### Nested if statements and elif statements
- Nested if/else statement
  ```py
  if condition:
    if another condition:
      do this
    else:
      do this
  else:
    do this
  ```
- if/elif/else statement
  - Can have as many `elif` conditions as we want
  ```py
  if condition1:
    do A
  elif condition2:
    do B
  elif condition3:
    do C
  else:
    do this
  ```

### Multiple if statements in succession
- Multiple if
  ```py
  if condition1:
    do A
  if condition2:
    do B
  if condition3:
    do C
  ```
- With if/elif/else statement, only one get executed
- With multiple if statements, multiple things will be executed if multiple conditions are met

### Logical operators
- `and` - A and B
  - Both A and B must be true to be evaluated to `True`
- `or` - A or B
  - Only one A or b need be true to be evaluated to `True`
- `not` - not E
  - Reverses the condition

### Exercise: Rollercoaster Ticket
- NOTE: line indentation matters a lot!!
  ```py
  print("Welcome to the rollercoaster!")
  height = int(input("What is your height in cm? "))
  bill = 0

  if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
      bill = 5
      print("Child tickets are $5.")
    elif age <= 18:
      bill = 7
      print("Youth tickets are $7.")
    # midlife crisis
    elif age >= 45 and age <= 55:
      print("Everything is going to be ok. Have a free ride on us!")
    else:
      bill = 12
      print("Adult tickets are $12.")

    # this if statement applies to everyone regardless of their age
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
      bill +=3

    print(f"Your final bill is ${bill}.")
  else:
    print("Sorry you cannot ride the rollercoaster.")
  ```

### Multi-block strings
- To print multiple lines of string, use a pair of 3-single quotes
  ```py
  print('''
  **********************
  Hello world!
  **********************
  ''')
  ```

### Day 3 Project: Treasure Island
```py
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_or_right = input("left or right? ").lower()
if left_or_right == "left":
  swim_or_wait = input("swim or wait? ").lower()
  if swim_or_wait == "wait":
    color = input("which color? yellow, blue, or red? ").lower()
    if color == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("Game Over.")
else:
  print("Game Over.")
```
