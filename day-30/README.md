# DAY 30 - Errors, Exceptions and Saving JSON Data

### Today's lessons:
- Handling errors and catching exceptions
- Raising your own exceptions 
- Write, read, and update JSON data
- Revisiting Password Manager project - handle exceptions and add search functionality

### Functions:
- `try`, `except`, `else`, `finally`, `raise` keywords
- json library:
  - Write: `json.dump()`
  - Read: `json.load()`
  - Update: `json.update()`

### Resources:
- Python json library docs: https://docs.python.org/3/library/json.html

### Catching exceptions: The try catch except finally pattern
- In the event something goes wrong with our program, we can catch these exceptions and handle them more gracefully without crashing our program
- Four keywords when handling exceptions:
  - `try` - Executing something that might cause an exception
  - `except` - Do this if there was an exception
  - `else` - Do this if there were no exceptions
  - `finally` - Do this no matter what happens. This will always be executed
  ```py
  # # FileNotFoundError
  # with open("a_file.txt") as file:
  # 	file.read()

  # # KeyError
  # a_dict = {"key": "value"}
  # value = a_dict["non_existent_key"]

  # # IndexError
  # fruit_list = ['Apple', 'Banana', 'Pear']
  # fruit = fruit_list[3]

  # # TypeError
  # text = "abc"
  # print(text + 5)

  try:
    # try to open the file and it doesn't exist
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    # try to find key that doesn't exist
    print(a_dict["ldjf"])
  except FileNotFoundError:  # catching the exception
    # if exception occurs, create the file
    file = open("a_file.txt", "w")
    file.write("Something")
  except KeyError as error_message:  # catch the exception and get hold of the error message
    print(f"The key {error_message} does not exist")
  else:  # do this if code in try block is successful
    content = file.read()
    print(content)
  finally:  # do this no matter what
    file.close()
    print('File was closed')
  ```

### Raising your own exceptions
- There are certain things that the machine will not be able to catch as errors because they are valid code. In this case, we can raise our own exceptions to catch the error
- Raise exception:
  - `raise` - Raise your own exceptions
  ```py
  height = float(input("Height: "))
  weight = int(input("Weight: "))

  if height > 3:
    # raise a ValueError class and provide a custom error message
    raise ValueError("Human height should not be over 3 meters.")

  bmi = weight / height ** 2
  print(f"BMI is: {bmi}")
  ```

### Exercise: IndexError handling
```py
fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and maker sure the code runs without crashing
def make_pie(index):
  try:
    fruit = fruits[index]
    print(fruit + " pie")
  except IndexError:
    print("fruit pie")

make_pie(4)
```

### Exercise: KeyError handling
```py
facebook_posts = [
  {'Likes': 21, 'Comments': 2},
  {'Likes': 13, 'Comments': 2, 'Shares': 1},
  {'Likes': 33, 'Comments': 8, 'Shares': 3},
  {'Comments': 4, 'Shares': 2},
  {'Comments': 1, 'Shares': 1},
  {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    # option 1
    pass
    # option 2
    total_likes += 0
    # option 3
    post['Likes'] = 0
		
print(total_likes)
```

### Exercise: Exception handling in the NATO Phonetic Alphabet project
- NATO Alphabet project from day 26. Handle exceptions when user enters characters other than the alphabets
- SOLUTION 1: Using while loop
  ```py
  import pandas

  data = pandas.read_csv("nato_phonetic_alphabet.csv")

  # TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
  phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
  # print(phonetic_dict)

  # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
  game_is_on = True
  while game_is_on:
    user_input = input(
      "Enter a word or type 'exit' to end: ").upper().replace(" ", "")

    # TODO 3. Catch the KeyError when a user enters a character that is not in the dictionary
    # Provide feedback to the user when an illegal word was entered
    # Continue prompting the user to enter another word until they enter a valid word
    if user_input != "EXIT":
      try:
        phonet_list = [phonetic_dict[letter] for letter in user_input]
      except KeyError:
        print("Sorry, only letters in the alphabet please.")
      else:
        print(phonet_list)
    else:
      game_is_on = False
  ```
- SOLUTION 2: Using function
  ```py
  import pandas

  data = pandas.read_csv("nato_phonetic_alphabet.csv")

  phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

  def generate_phonetic():
    user_input = input(
              "Enter a word or type 'exit' to end: ").upper().replace(" ", "")
    if user_input != "EXIT":
      try:
        phonet_list = [phonetic_dict[letter] for letter in user_input]
      except KeyError:
        print("Sorry, only letters in the alphabet please.")
        # Ask for user to enter a word again
        generate_phonetic()
      else:
        print(phonet_list)
        # Ask for user to enter a word again
        generate_phonetic()
    else:
      game_is_on = False

  generate_phonetic()
  ```

### Write, read, and update JSON data in the Password Manager project
- JSON stands for JavaScript Object Notation and is a type of data format. It is one of the most popular ways to transfer data across the internet and has been adopted by many programming languages
- JSON format looks very similar to Python dictionary. It has key-value pair data structure
- **Serialize** - writing data to json format
- **Deserialize** - convert json-format data to other forms
- Python json library docs: https://docs.python.org/3/library/json.html
- Python has in-built json library for formatting data
- Built-in functions from the json library:
  - Write: `json.dump()`
  - Read: `json.load()`
  - Update: `json.update()`
- **Writing json data:**
  - The json.dump() method to write data in json format. This process is serializing data to json format
  ```py
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  with open("data.json", "w") as data_file:
    # 1st arg is the data to write
    # 2nd arg is the file to write to
    # 3rd arg is formatting the json data
    json.dump(new_data, data_file, indent=2)
  ```
- **Reading json data:**
  - The json.load() method is to read json data
  - When reading json data, Python automatically converts the data into a dictionary data type. This process is deserialize json data to Python dictionary
  ```py
  with open("data.json", "r") as data_file:
    data = json.load(data_file)
    print(type(data))  # <class 'dict'>
  ```
- **Updating json data:**
  - The json.update() method updates or appends new data to the json file
  ```py
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  with open("data.json", "r") as data_file:
    # Reading old data
    data = json.load(data_file)
    # Updating old data with new data
    data.update(new_data)
  ```

### Day 30 project: Password Manager v2
- At the moment, we save the website, email, and password data in a text file. What we want to do is add a Search button that allows users to enter a website name and retrieve the email and password information shown in a pop up window
- Secondly, a text file is very difficult to work with in terms of searching, updating, and formatting the file. We want to save the data in a json file format instead so that we can read, write, and update the file
- Lastly, apply handling exceptions. When we try to write data to a json file and if that file doesn't exist, our program will crash
- Handling exceptions:
  ```py
  def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
      website: {
        "email": email,
        "password": password
      }
    }

    if website == "" or password == "":
      messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
      # TODO: Modify the code to handle the FileNotFoundError
      # Create a new data.json file if it does not exist
      # If the file already exists, then simply add the new entry
      try:
        with open("data.json", "r") as data_file:
          # Reading old data
          data = json.load(data_file)
      except FileNotFoundError:
        with open("data.json", "w") as data_file:
          json.dump(new_data, data_file, indent=2)
      else:
        # Updating old data with new data
        data.update(new_data)

        # Saving updated data
        with open("data.json", "w") as data_file:
          # 1st arg is the data to write
          # 2nd arg is the file to write to
          # 3rd arg is formatting the json data
          json.dump(data, data_file, indent=2)
      finally:
        website_entry.delete(0, END)
        website_entry.focus()
        password_entry.delete(0, END)
  ```
- Add search functionality:
  ```py
  from tkinter import messagebox

  # ---------------------------- SEARCH PASSWORD ------------------------------- #
  # 1. Add a "Search" button next to the website entry field
  # 2. Adjust the layout and the other widgets as needed to get the desired look
  # 3. Create a function called find_password() that gets triggered when the "Search" button is pressed
  # 4. Check if the user's text entry matches an item in the data.json
  # 5. If yes, show a messagebox with the website's name and password
  # 6. Catch an exception that might occur trying to access the data.json show a messagebox with the text:
  #    "No Data File Found"
  # 7. If the user's website does not exist inside the data.json, show a messagebox that reads
  #    "No details for the website exists"
  def find_password():
    website = website_entry.get()
    try:
      with open("data.json", "r") as file:
        data = json.load(file)
    except FileNotFoundError:
      messagebox.showerror(title="Error", message="No Data File Found")
    else:
      if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website.title(), message=f"Email: {email}\nPassword: {password}")
      else:
        messagebox.showerror(title="Not Found", message=f"No details for the {website} exists.")
    finally:
      website_entry.delete(0, END)


  # ---------------------------- UI SETUP ------------------------------- #
  search_btn = Button(text="Search", highlightbackground="white", command=find_password, width=14)
  search_btn.grid(row=1, column=2)
  ```