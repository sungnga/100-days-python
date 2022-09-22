# DAY 7: Hangman

#### Today's lessons:
- Flowchart programming
- Importing modules

#### Functions:
- if/in

#### Import modules
- File: hangman_words.py
  - Contains `word_list` list
- File: hangman_art.py
  - Contains `stages` list and `logo` string
- File: main.py
  - Option 1:
    ```py
    # Import the module
    import hangman_art

    # Use the module
    hangman_art.stages
    hangman_art.stages[lives]
    ```
  - Option 2:
    ```py
    import random
    # Import items from module
    from hangman_art import stages, logo
    from hangman_words import word_list

    # Use the items
    print(logo)
    chosen_word = random.choice(word_list)
    ```

#### Challenge 1 - Picking a random word and checking answer
- Step 1 -> `word_list = ["aardvark", "baboon", "camel"]`
- TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
- TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
- TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
```py
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

if guess in chosen_word:
  print("Right")
else:
  print("Wrong")
```

#### Challenge 2 - Replacing blanks with guesses
- TODO-1: - Create an empty List called display.
  - For each letter in the chosen_word, add a "_" to 'display'.
  - So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
- TODO-2: - Loop through each position in the chosen_word;
  - If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  - e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  ```py
  for letter in chosen_word:
    if letter == guess:
      print("Right")
    else:
      print("Wrong")
  ```
- TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  - Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
```py
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

if guess in chosen_word:
  print(True)
else:
  print(False)

display = []
for letter in chosen_word:
  display += "_"
print(display)

for i in range(0, len(chosen_word)):
  if chosen_word[i] == guess:
    display[i] = guess
print(display)
```

#### Challenge 3 - Checking if the player has won
```py
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# Create blanks
display = []
for letter in chosen_word:
  display += "_"
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  # Check guessed letter
  for i in range(len(chosen_word)):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter
  print(display)

  # Check if user has got all letters
  if '_' not in display:
    end_of_game = True
    print("You win.")
```

#### Challenge 4 - Keeping track of the player's lives
```py
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for i in range(len(chosen_word)):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter
  print(display)
  
  #TODO-2: - If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1. 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(stages[lives])
```

#### Challenge 5 - Improving the user experience
- File: hangman_art.py
- File: hangman_words.py
- File: main.py
  ```py
  import random
  from hangman_words import word_list
  from hangman_art import logo, stages

  #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
  #Delete this line: word_list = ["aardvark", "baboon", "camel"]
  chosen_word = random.choice(word_list)

  end_of_game = False
  lives = 6

  #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
  print(logo)

  #Testing code
  print(f'Pssst, the solution is {chosen_word}.')

  #Create blanks
  display = []
  for letter in chosen_word:
    display += "_"

  while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}.")
    
    #Check guessed letter
    for i in range(len(chosen_word)):
      letter = chosen_word[i]
      if letter == guess:
        display[i] = letter
    # print(display)
    
    #Check if user is wrong
    if guess not in chosen_word:
      #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
      end_of_game = True
      print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
  ```