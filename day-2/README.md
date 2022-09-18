## Day 2 - Data Types and Type Manipulation

#### Today's lessons:
- Data types
- Converting types
- f-strings
- Mathematical operations
- Project: Tip Calculator

#### Functions:
- type()
- str(), float(), int(), round()
- f" {variable}"

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