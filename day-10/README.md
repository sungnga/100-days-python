# DAY 10 - Functions with Outputs

### Today's lessons:
- Function with output
- return keyword
- Function with multiple return values
- Early return
- Docstrings
- Print vs return
- Recursion
- Store functions in a dictionary

### Functions:
- .title() -> Turns the first letter of a word into uppercase

### Functions with outputs
- A function with output allows you to have an output once the function is completed. The output keyword of a function is `return`. What comes after the `return` keyword is the output returned from the function
- Any code after the `return` keyword in the function will not get executed
- When we call a function, we can save the output from the function to a variable
  ```py
  # Function with output
  def my_function():
    result = 3 * 2
    return result

  # Save the output to a variable
  output = my_function() #output = 6
  ```
- Example:
  ```py
  def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

  print(format_name("NGA", "LA")) # Nga La
  ```

### Multiple return values
- We can have multiple return values in a function. This is useful when we have conditional statements where we want to exit out of the function early if the condition isn't met. This is called "early return" or "early exit"
```py
# Return as an early exit
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
```

### Exercise: Days in Month
```py
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
  if input_month > 12 or input_month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(input_year) and input_month == 2:
    return 29
  return month_days[input_month - 1 ]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

### Docstrings
- Docstrings is a way for us to create documentation in our function or block of code
- The docstring has to go as the **first** indented line after the declaration and must be inside a pair of **triple quotation mark** `"""<doctstring>"""`
```py
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name"""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
```

### Calculator part 1: Combining dictionaries and functions
```py
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Store functions in a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
cal_function = operations[operation_symbol]
answer = cal_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
```

### Print vs return
- By using the `return` keyword to return the output from a function, we preserve the value in the output and use it on other tasks. For example, we can pass the output of one function as input to another function

### Calculator part 2: While loops, flags, and recursion
- Set a flag and then ask the user if they want to continue calculating with the current result
- If they choose to continue, use a while loop and ask the user for the next operation symbol and the next number and perform another operation until the user chooses to stop
- If the user chooses to stop the calculation, we bring them back to the start of the calculation. We continue this cycle using recursion function
```py
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Store functions in a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  not_finished = True

  while not_finished:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    cal_function = operations[operation_symbol]
    answer = round(cal_function(num1, num2), 2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if should_continue == "y":
      num1 = answer
    elif should_continue == "n":
      not_finished = False
      calculator()

calculator()
```

### Calculator part 3: Finishing touches and bug fixes
- Print out the calculator art when the program starts
- Change the code so that the program can accept user's input that contain decimals
- File: calculator_art.py
- File: main.py
  ```py
  from calculator_art import logo

  # Add
  def add(n1, n2):
    return n1 + n2

  # Subtract
  def subtract(n1, n2):
    return n1 - n2

  # Multiply
  def multiply(n1, n2):
    return n1 * n2

  # Divide
  def divide(n1, n2):
    return n1 / n2

  # Store functions in a dictionary
  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }

  def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    not_finished = True

    while not_finished:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))
      cal_function = operations[operation_symbol]
      answer = cal_function(num1, num2)

      print(f"{num1} {operation_symbol} {num2} = {answer}")

      should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
      if should_continue == "y":
        num1 = answer
      elif should_continue == "n":
        not_finished = False
        calculator()

  calculator()
  ```
