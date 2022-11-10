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
