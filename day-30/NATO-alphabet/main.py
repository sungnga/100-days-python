# SOLUTION 1
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


# SOLUTION 2
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
