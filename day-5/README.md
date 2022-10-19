# Day 5 - For Loops

### Today's lessons:
- For loops
- The range() function
- Modulo operation

### Functions:
- range()

### For loop
```py
for item in list_of_items:
  #Do something to each item
```
- By using a loop, we can go through each item on a list and perform some action with each individual item
- **NOTE: When looping through a list, each item IS the value of that item**
  ```py
  fruits = ["Apple", "Peach", "Pear"]
  for fruit in fruits:
    print(fruit) # Apple
    print(fruit + " Pie") # Apple Pie
  ```

### Exercise: Average Height
```py
# Write a program that calculates the avg student height from a list of heights
student_heights = input("Input a list of student heights ").split() # array of strings

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # array of integers

total_height = 0
number_of_students = 0
for height in student_heights:
  total_height += height
  number_of_students += 1
avg_height = round(total_height / number_of_students)
print(avg_height)
```

### Exercise: High Score
```py
# Write a program that calculates the highest score from a list of scores
student_scores = input("Input a list of student scores ").split() # array of strings
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n]) # array of integers

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")
```

### for loops, the range() function
- The range() function generates a range of numbers
- for loop with range
  - NOTE: The range function does not include the stop number. For example, if a range is between 1 and 10, 10 is not included
  - Has the option to pass in a 3rd argument for step size if you want to change the default step size of 1
  ```py
  for item in range(start, stop[, step],): # step arg is optional. By default, it increments by 1
    print(item)
  ```
- Example:
  ```py
  # Sum up the numbers between 1 and 100
  total = 0
  for number in range(1, 101):
    total += number
  print(total)
  ```

### Exercise: Add Even Numbers
```py
# Write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100
total = 0
for num in range(2, 101, 2):
  # print(num)
  total += num
print(total)
```

### Exercise: The FizzBuzz Job Interview Question
```py
# Counting from number 1 to 100, write a program that prints "Fizz" if the number is divisible by 3, prints "Buzz" if divisible by 5, and prints "FizzBuzz" if divisible by 15
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
```

### Day 5 project: Password Generator
```py
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for char in range(1, nr_letters + 1):
  password += letters[random.randint(0, len(letters) - 1)]
  # password += random.choice(letters)

for symb in range(1, nr_symbols + 1):
  password += symbols[random.randint(0, len(symbols) - 1)]
  # password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
  password += numbers[random.randint(0, len(numbers) - 1)]
  # password += random.choice(numbers)

random.shuffle(password)
shuffled_password = ''.join(password)
print(f"Your password is: {shuffled_password}")
```
