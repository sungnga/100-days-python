# DAY 8 - Function Parameters

#### Today's lessons:
- Functions with inputs
- Arguments and parameters

#### Functions:


#### Functions with inputs
- Simple function:
  ```py
  def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
  greet()
  ```
- Function that allows for input:
  - We create a function that carries out some instructions. But every time we execute it, we get to modify it a little bit by changing the input
  - The input is the data that the function will receive
  - When defining the function, the name of the data that's being passed in is called ***parameter***. We use the name inside the function to refer to it and to do things with it
  - When we call the function, the actual value of data that we pass to the function is called ***argument***
  ```py
  def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
  greet_with_name("Nga")
  ```

#### Positional vs keyword
- Functions with more than 1 input:
  - Separate multiple parameters with commas
- The ***positional arguments*** match with the positional parameters
  - a = 1, b = 2, c = 3
  ```py
  def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
  my_function(1, 2, 3)
  ```
- With ***keyword arguments***, we bind the arguments to the parameters. With keyword arguments, the order of the arguments we pass to the function call doesn't matter
  - Using keyword argument is less error-prone, but makes your code a little longer
  ```py
  def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
  my_function(c=3, a=1, b=2)
  ```
- Example: Function with multiple inputs and using keyword arguments
  ```py
  def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

  # Using keyword arguments
  greet_with(location="San Francisco", name="Nga")
  ```

#### Exercise: Paint area calculator
```py
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height X wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 X 4) ÷ 5
# Define a function called paint_calc() so that the code below works.  

import math
def paint_calc(height, width, cover):
  num_of_cans = (height * width) / cover
  # print(num_of_cans)
  rounded_cans = math.ceil(num_of_cans)
  print(f"You'll need {rounded_cans} cans to paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```

#### Exercise: Prime Number Checker
- Prime numbers are numbers that can only be cleanly divided by itself and 1
```py
def prime_checker(number):
  isPrime = True
  
  if number <= 1:
    isPrime = False

  for i in range(2, number):
    if n % i == 0:
      isPrime = False

  if isPrime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)
```

### Day 8 project: Caesar Cipher
#### Part 1
```py

```