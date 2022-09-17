## DAY 1 - Working with Variables to Manage Data

#### The print() function
- Printing to the console
- `print("What you want to print")`

#### String manipulation
- Add new line to a string using `\n`
  - `print("Hello world\nHello world\nHello world")`
- Concatenate two or more strings into one using a `+` sign

#### The input() function
- input() will get user input in console
- `input("A prompt for the user")`

#### Step by step into code
- www.thonny.org
- A Python debugger tool that lets you step through your code and see how the computer evaluates your code

#### Comment code in Python
- Use the `#` sign in front of your text
- Comments will not be executed
- `Cmd + /` to turn a line into comment

#### The len() function
- `len()` calculates the number of characters in a string
- `len("Jack")`

#### Exercise:
- `print( len( input("What is your name? ") ) )`
- First, get input from user. Then calculate its length. Lastly, print the result to console

#### Variables
- Use variables to store a piece of data
- Give the variable a name so you can retrieve the data by referring to the variable name
- Example:
  ```py
  name = input("What is your name?")
  length = len(name)
  print(length)
  ```

#### Variable naming
- Separate words with underscore `_`
  - `user_name`
- When naming variables,
  - cannot have spaces
  - cannot start with a number
  - try not to use reserved keywords such as print, input, etc

### Day 1 Project: Band name generator
1. Create a greeting for your program
  - `print("Welcome to the band name generator")`
2. Ask the user for the city that they grew up in
  - `city = input("What city did you grow up in?\n")`
3. Ask the user for the name of a pet
  - `pet = input("What is the name of your pet?\n")`
4. Combine the name of their city and pet and show them their band name
  - `print("Your band name is " + city + " " + pet)`
5. Make sure the input cursor shows on a new line

----------------------------

## Day 2 - Data Types and Type Manipulation

#### Primitive data types
- **String**
  - Strings are surrounded by single or double quotation
  - Subscript: is a method of pulling a particular element out of a string. `"Hello"[4]`
  - Use the plus sign `+` to concatenate strings together. `print("Nga" + "La")`
- **Integer**
  - Integers are whole numbers, no matter positive or negative
  - Use the plus sign `+` to calculate. `print(123 + 345)`
- **Float**
  - Numbers with decimal is a floating point number. `342.45631`
  - Use underscore `_` to separate digits for human readability. `503_366_1` -> `503,366,1`
- **Boolean**
  - Can only have two possible values: `True` or `False`

#### Type error, type checking and type conversion
- `type()` is a type-check function used to check for data type
- Type conversion or type casting is converting one data type to another
  - `str(123)` -> `"123"`
  - `float("100.5")` -> `100.5`
  - `int("898")` -> `898`
- Example:
  ```py
  # num_char is an int type
  num_char = len(input("What is your name?"))

  # new_num_char is a string type
  new_num_char = str(num_char)

  # would get a type error if new_num_char is an int data type
  print("Your name has " + new_num_char + " characters.")
  ```

#### Mathematical operations
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponent: `**`
- The order of operations matters here: PEMDAS. P is parenthesis
- Exercise: calculate BMI
  ```py
  height = input("Enter your height in m: ")
  weight = input("Enter your weight in kg: ")

  # BMI = weight(kg) / height^2(m^2)
  bmi = int(weight) / float(height) ** 2
  bmi_as_int = int(bmi)
  print(bmi_as_int)
  ```

#### Number manipulation and F strings
- `round(arg1, arg2)` is a function that rounds a number to a whole number or to a specified number of decimal places
  - `round(2.6667, 2)` -> `2.67`
- `//` is a floor division where it chops off the remaining decimal. The data type is an ***integer***
- When doing a ***division*** operation, the data type of the result is a ***float***
- The data type of the ***value*** from the `input()` function is a ***string***
- A shorthand operation to manipulate a value based on its previous value: +=, -=, *=, /=
- f-string is a handy shortcut of inserting different data types into a string
  - Write the letter `f` in front of a double or single quotation and then put the variable inside a pair of curly braces
  ```py
  score = 0
  height = 1.8
  isWinning = True
  # f-string
  print(f"Your score is {score}, your height is {height}, your are winning is {isWinning}")
  # Your score is 0, your height is 1.8, your are winning is True
  ```

#### Exercise: Life in weeks
```py
age = input("What is your age? ")

age_as_int = int(age)

years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
```

### Day 2 Project: Tip Calculator
```py
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_ppl = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
print(bill_with_tip)
per_person = bill_with_tip / total_ppl
# round to two decimal places
final_amt = round(per_person, 2)
# format with two decimal places
final_amt = "{:.2f}".format(final_amt)
message = f"Each person should pay: ${final_amt}"
print(message)
```

----------------------------

## Day 3 - Control Flow and Logical Operations

#### Today's lessons:
- Conditional statements
- Logical operators
- Code blocks
- Scope

#### Control flow with if/else and conditional operator
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
- One equal `=` means ***assignment***
- Two equals `==` means ***check equality***
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

#### Nested if statements and elif statements
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

#### Multiple if statements in succession
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

#### Logical operators
- `and` - A and B
  - Both A and B must be true to be evaluated to `True`
- `or` - A or B
  - Only one A or b need be true to be evaluated to `True`
- `not` - not E
  - Reverses the condition

#### Exercise: Rollercoaster Ticket
- NOTE: line of indentation matters a lot!!
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

#### Multi-block strings
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

----------------------------
