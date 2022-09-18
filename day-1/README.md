## DAY 1 - Working with Variables to Manage Data

#### Today's lessons:
- print() and input() functions
- Variables, variable naming rules
- Comment code
- Project: Band Name Generator

#### Functions:
- print()
- input()
- len()

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

### Day 1 Project: Band Name Generator
1. Create a greeting for your program
  - `print("Welcome to the band name generator")`
2. Ask the user for the city that they grew up in
  - `city = input("What city did you grow up in?\n")`
3. Ask the user for the name of a pet
  - `pet = input("What is the name of your pet?\n")`
4. Combine the name of their city and pet and show them their band name
  - `print("Your band name is " + city + " " + pet)`
5. Make sure the input cursor shows on a new line