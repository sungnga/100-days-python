# DAY 9 - Dictionaries and nesting

#### Today's lessons:
- Dictionaries
- Nesting lists

#### Functions:


#### Dictionary
- Python dictionary is very similar to real life dictionary
- A dictionary comes with key-value pair. The key is the word and the value is the definition associated with that word
- **Creating a dictionary:**
  - `{key: value}`
- Separate multiple entries in a dictionary with a comma: `,`
  ```py
  programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
  }
  ```
- **Retrieving items from dictionary:**
  - Dictionaries have elements which are identified by their key. We fetch items from the dictionary by their key. Add the square bracket to the dictionary and give it the key. It will return the value of that key
  - `dictionary_name[key]`
  - IMPORTANT!: Make sure to use the correct data type for key
- **Adding new items to dictionary:**
  - Add the square bracket and give it a key. Then assign it to a value
  - IMPORTANT!: Watch out for the data type of key and value
  - `dictionary_name[key] = value`
- **Create an empty dictionary:**
  - `empty_dictionary = {}`
  - `empty_list = []`
- **Wipe an existing dictionary:**
  - Wipe an existing dictionary by assigning to an empty dictionary
    - `dictionary_name = {}`
  ```py
  programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
  }
  programming_dictionary = {}
  ```
- **Edit an item in a dictionary:**
  - Editing an item is similar to adding an item to a dictionary
  - Fetch the item by its key and assigning it to a new value
    - `dictionary_name[key] = new_value` 
  - The program looks into the dictionary and tries to find the item by its key. If the item exists, it'll replace the value data. If the item doesn't exist, it'll create the item
- **Loop through a dictionary:**
  - Looping through a dictionary will return the key, but we can use that key to retrieve its value from the dictionary
  ```py
  for key in dictionary_name:
    print(key)
    print(dictionary_name[key]) #Retrieving the value
  ```

#### Exercise: Grading program
```py
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.
for student in student_scores:
  score = student_scores[student]
  if score >= 91:
    student_grades[student] = "Outstanding"
  elif score >= 81:
    student_grades[student] = "Exceeds Expectations"
  elif score >= 71:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)
```

#### Nesting lists and dictionaries
- Nesting a List and a Dictionary in a dictionary 
  ```py
  {
    Key: [List],
    Key2: {Dict},
  }
  ```
- Nesting dictionary in a dictionary
  ```py
  travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Suttgart"], "total_cities": 15},
  }
  ```
- Nesting dictionaries in a list
  - Retrieve an item in a list by their index
  - Retrieve an item in a dictionary by their key
  ```py
  [{
    Key: [List],
    Key2: {Dict},
  },
  {
    Key: Value,
    Key2: Value,
  }]
  ```

#### Exercise: Dictionary in list
```py
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {"country": country_visited, "visits": times_visited, "cities": cities_visited}
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
```

### Day 9 project: The Secret Auction