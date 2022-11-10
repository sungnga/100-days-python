# DAY 26 - List and Dictionary Comprehensions

### Today's lessons:
- List comprehension
- Dictionary comprehension 

### Functions:
- `new_list = [new_item for item in list]`
- `new_list = [new_item for item in list if test]`
- `new_dict = {new_key: new_value for item in list}`
- `new_dict = {new_key: new_value for (key,value) in dict.items()}`
- `new_dict = {new_key: new_value for (key,value) in dict.items() if test}`
- .split()
- .iterrows()

### How to create lists using list comprehension
- **List comprehension:**
  - `new_list = [new_item for item in list]`
  - Perform new_item task for each item in list. Save the result in new_list
  ```py
  # For loop
  numbers = [1, 2, 3]
  new_list = []
  for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
  print(new_list)  # [2, 3, 4]

  # List comprehension
  numbers = [1, 2, 3]
  new_list = [n + 1 for n in numbers]
  print(new_list)  # [2, 3, 4]

  # Working with string
  name = "Angela"
  letters_list = [letter for letter in name]
  print(letters_list)  # ['A', 'n', 'g', 'e', 'l', 'a']

  # Working with range
  range_list = [n * 2 for n in range(1, 5)]
  print(range_list)  # [2, 4, 6, 8]
  ```
- **Python sequences:** 
  - list, range, string, tuple
- **Conditional list comprehension:**
  - `new_list = [new_item for item in list if test]`
  - Perform new_item task for each item in list, only if test condition is met
  ```py
  # Create a new list that contains names less than 5 characters
  names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
  short_names = [name for name in names if len(name) < 5]
  print(short_names)  # ['Alex', 'Beth', 'Dave']

  # Create a new list that contains the names longer than 5 chars in all caps
  names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
  long_names = [name.upper() for name in names if len(name) > 5]
  print(long_names)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']
  ```

### Exercise: Squaring numbers
```py
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

### Exercise: Filtering even numbers
```py
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)  # [2, 8, 34]
```

### Exercise: Data overlap
- Files: file1.txt, file2.txt
```py
with open("file1.txt") as file1:
	file1_data = file1.readlines()
	new_list_1 = [int(n.strip()) for n in file1_data]
	print(new_list_1)  # [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]

with open("file2.txt") as file2:
	file2_data = file2.readlines()
	new_list_2 = [int(n.strip()) for n in file2_data]
	print(new_list_2)  # [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

# Solution 1
overlap_nums = [num for num in new_list_1 if num in new_list_2]
print(overlap_nums)  # [3, 6, 5, 33, 12, 7, 42, 13]

# Solution 2
result = [int(num.strip()) for num in open("file1.txt").readlines() if num in open("file2.txt").readlines()]
print(result)  # [3, 6, 5, 33, 12, 7, 42, 13]

# Solution 3
lapping = [int(num) for num in file1_data if num in file2_data]
print(lapping)  # [3, 6, 5, 33, 12, 7, 42, 13]
```

### Apply list comprehension to the U.S. State Game
```py
if answer == "Exit":
  # Save the missing states to a .csv file
  # Using for loop
  # missing_states = []
  # for state in states:
  # 	if state not in guessed_states:
  # 		missing_states.append(state)

  # Using list comprehension
  missing_states = [state for state in states if state not in guessed_states]

  data_dict = {
    "Missed States": missing_states
  }
  # Create dataframe and save to cvs file
  pandas.DataFrame(data_dict).to_csv("missed_states.csv")
  break
```

### How to use dictionary comprehension
- NOTE: a list is denoted by square brackets `[]` and a dictionary is denoted by curly brackets `{}`
- `new_dict = {new_key: new_value for item in list}`
- `new_dict = {new_key: new_value for (key,value) in dict.items()}`
- `new_dict = {new_key: new_value for (key,value) in dict.items() if test}`
```py
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Create a dictionary that contains students with random scores
students_scores = {student: random.randint(30, 100) for student in names}
print(students_scores)  # {'Alex': 33, 'Beth': 64, 'Caroline': 80, 'Dave': 30, 'Eleanor': 88, 'Freddie': 88}

# Create a dictionary with students with score above 60
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)  # {'Beth': 64, 'Caroline': 80, 'Eleanor': 88, 'Freddie': 88}
```

### Exercise: Dictionary comprehension 1
```py
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
print(words_list)  # ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
result = {word: len(word) for word in words_list}
print(result)  # {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
```

### Exercise: Dictionary comprehension 2
```py
weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
```

### How to iterate over a Pandas DataFrame
```py
student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
  print(key)
  print(value)

# Iterate through Pandas data frame
import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Looping through a data frame
for (key, value) in student_dataframe.items():
  print(key)
  print(value)

# Loop through rows of a data frame
for (index, row) in student_dataframe.iterrows():
  print(index)
  print(row)  # each row is a pandas series object
  print(row.student)
  print(row.score)
  if row.student == "Angela":
    print(row.score)
```

### Day 26 project: NATO Alphabet
- `new_dict = {new_key:new_value for (index, row) in df.iterrows()}`
```py
# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

game_is_on = True
while game_is_on:
  user_input = input("Enter a word: ").upper().replace(" ", "")
  if user_input != "EXIT":
    phonet_list = [phonetic_dict[letter] for letter in user_input if letter in phonetic_dict.keys()]
    print(phonet_list)
  else:
    game_is_on = False
```