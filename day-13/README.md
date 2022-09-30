# DAY 13 - Debugging

#### Today's lessons: How to fix bugs
- Step 1: Describe the problem
- Step 2: Reproduce the bug
- Step 3: Play computer
- Step 4: Fix the errors, watch for red underlines
- Step 5: Print() statement is your friend
- Step 6: Use a debugger

#### Links:
- Python Tutor - a debugger tool: https://pythontutor.com/visualize.html#mode=edit

#### Step 1: Describe the problem
```py
def my_function():
  #The range() function DOES NOT include the upper bound number
  # for i in range(1, 20):
  for i in range(1, 21): #Bug fixed
    if i == 20:
      print("You got it")
my_function()
```

#### Step 2: Reproduce the bug
```py
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #A list starts at index 0 and ends at index 5
# dice_num = randint(1, 6) #choose random int between 1 and 6, including both end points
dice_num = randint(0, 5) #Bug fixed: shift the range
print(dice_imgs[dice_num])
```

#### Step 3: Play computer and evaluate each line
```py
#Bug: if input year is 1994, nothing prints out. 
#Because both if statements make 1994(input year) equal to False
year = int(input("What's your year of birth?: "))
#To fix bug: set one of the if statements to include 1994
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```

#### Step 4: Fix the errors and watch for red underlines
- When the code editor or the console is giving you an error, fix the errors before continue
- The editor will highlight the error with red underline. Hover over it to read the error message
- If the error produced in the console, one way to solve the error is copy the entire error message and paste it into Google. Most likely other programmers have encountered the same issue
- Example code with bugs:
  - Bug #1: The 2nd print() statement should be indented
  - Bug #2: The output from an input() function is a string. Cannot perform a comparison between a string-type value and an integer-type value
  - Bug #3: Need to use the f-string to print the variable in a string. Harder to catch the bug
  ```py
  age = input("How old are you?")
  if age > 18:
  print("You can drive at age {age}.")
  ```
- 1st bug printed in the console:
  ```py
    File "main.py", line 33
      print("You can drive at age {age}.")
      ^
  IndentationError: expected an indented block
  ```
- 2nd bug printed in the console:
  ```py
  How old are you? 24
  Traceback (most recent call last):
    File "main.py", line 32, in <module>
      if age > 18:
  TypeError: '>' not supported between instances of 'str' and 'int'
  ```
- 3rd bug is harder to detect and debug because you need to rely on your skills as a programmer
  ```py
  #Need to use the f-string to print the value from the variable age
  print("You can drive at age {age}.")
  print(f"You can drive at age {age}.")
  ```

#### Step 5: Squash bugs with a print() statement
- Code with bugs
  ```py
  pages = 0
  word_per_page = 0
  pages = int(input("Number of pages: "))
  total_words = pages * word_per_page
  print(total_words)
  ```
- Use print() statement to see the values
  ```py
  pages = 0
  word_per_page = 0
  pages = int(input("Number of pages: "))
  #Bug: == means comparison, not assignment
  #The output for == is either True or False
  output = word_per_page == int(input("Number of words per page: "))
  print(f'word_per_page = {word_per_page}')
  print(f"pages = {pages}")
  print(f"{output = }")
  total_words = pages * word_per_page
  print(total_words)
  ```

#### Step 6: Use a debugger
- Use a debugger tool like Python Tutor to step through your code line by line
- Python Tutor link: https://pythontutor.com/visualize.html#mode=edit
  - Add a break point by clicking on the line of code to examine that particular line of code

#### Final debugging tips
- Step 7: Take a break
  - Go do something else
  - Take a nap
  - Go to sleep and tackle the problem again tomorrow
- Step 8: Ask a friend
- Step 9: Run often
  - Run your code often. Don't wait until you've written too many lines of code
  - Confirm that the code is doing what you want it to do. Don't wait for bugs to pile up
- Step 10: Ask stackOverflow

#### Exercise: Debugging Odd or Even
- Starter code with bugs
  ```py
  number = int(input("Which number do you want to check?: "))

  if number % 2 = 0:
    print("This is an even number.")
  else:
    print("This is an odd number.")
  ```
- Bug fixed
  ```py
  number = int(input("Which number do you want to check?: "))

  #Bug: need a comparison symbol, not an assignment
  if number % 2 == 0:
    print("This is an even number.")
  else:
    print("This is an odd number.")
  ```

#### Exercise: Debugging Leap Year
- Starter code with bugs
  ```py
  year = input("Which year do you want to check?: ")

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")
  ```
- Bug fixed
  ```py
  #Bug: the output from input() function is a string. Need to convert it to an int
  year = int(input("Which year do you want to check?: "))

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")
  ```

#### Exercise: Debugging FizzBuzz
- Starter code with bugs
  ```py
  for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
      print("FizzBuzz")
    if number % 3 == 0:
      print("Fizz")
    if number % 5 == 0:
      print("Buzz")
    else:
      print([number])
  ```
- Bug fixed
  ```py
  for number in range(1, 101):
    #Bug1: what we want is if the number is divisible by 3 AND 5, print "FizzBuzz"
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    #Bug2: number 15 will print "FizzBuzz", "Fizz", and "Buzz", not the expected "FizzBuzz"
    #because it satisfies all 3 if statements
    #Need to use elif instead
    elif number % 3 == 0:
      print("Fizz")
    elif number % 5 == 0:
      print("Buzz")
    #Bug3: this else statement only applies to the last if statement, not all 3 if statements
    #Number 6 will print "Fizz" and "[6]" because it is divisible by 3 however not divisible by 5
    #Change the last if statement to elif
    else:
      print([number])
  ```


