# DAY 8 - Function Parameters

#### Today's lessons:
- Functions with inputs
- Arguments and parameters
- Positional vs keyword arguments

#### Functions:
- Simple function: my_function()
- Function that allows input: my_function(input)
- Function with more than 1 input: my_function(input1, input2, input3)

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
#### Part 1 - Encryption
```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    ##Bug alert: What happens if you try to encode the word 'civilization'?
def encrypt(plain_text, shift_amt):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amt
    if new_position > 25:
      new_position = new_position - 26
    new_letter = alphabet[new_position] 
    print(f"{letter} {position} = {new_letter}")
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amt=shift)
```

#### Part 2 - Decryption
```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amt):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amt
    if new_position > 25:
      new_position = new_position - 26
    new_letter = alphabet[new_position]
    print(f"{letter} {position} {new_position} {new_letter}")
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decrypt(plain_text, shift_amt):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amt
    if new_position < 0:
      new_position = new_position + 26
    new_letter = alphabet[new_position]
    print(f"{letter} {position} {new_position} {new_letter}")
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amt=shift)
elif direction == "decode":
  decrypt(plain_text=text, shift_amt=shift)
```

#### Part 3 - Refactor
```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_amt, cipher_direction):
  end_text = ""
  
  for letter in start_text:
    position = alphabet.index(letter)

    if cipher_direction == "encode":
      new_position = position + shift_amt
    elif cipher_direction == "decode":
      new_position = position - shift_amt
      
    if new_position > 25:
      new_position = new_position - 26
    if new_position < 0:
      new_position = new_position + 26
      
    new_letter = alphabet[new_position]
    # Testing output
    print(f"{letter} {position} {new_position} {new_letter}")
    end_text += new_letter

  print(f"The {cipher_direction}d text is {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amt=shift, cipher_direction=direction)
```

#### Part 4 - Improve user experience and final touches
- File: art.py
- File: main.py
  ```py
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def caesar(start_text, shift_amt, cipher_direction):
    end_text = ""
    for char in start_text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if char in alphabet:
        position = alphabet.index(char)
        if cipher_direction == "encode":
          new_position = position + shift_amt
        elif cipher_direction == "decode":
          new_position = position - shift_amt
          
        if new_position > 25:
          new_position = new_position - 26
        if new_position < 0:
          new_position = new_position + 26
        
        new_char = alphabet[new_position]
        # Testing output
        print(f"{char} {position} {new_position} {new_char}")
        end_text += new_char
      else:
        end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")

  #TODO-1: Import and print the logo from art.py when the program starts.
  from art import logo
  print(logo)

  #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
  #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
  #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
  #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
  start_again = True
  while start_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26
    
    caesar(start_text=text, shift_amt=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
      start_again = False
      print("Goodbye")
  ```