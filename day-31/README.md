# DAY 31 - Flash Card App Capstone Project

### Resources:
- Pandas DataFrame docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

### Step 1: Create the User Interface (UI) with Tkinter
```py
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 265, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

# Text
canvas.create_text(400, 160, text="french", fill="black", font=LANGUAGE_FONT)
canvas.create_text(400, 280, text="word", fill="black", font=WORD_FONT)


# Buttons
wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, borderwidth=0, highlightthickness=0)
wrong_btn.grid(row=1, column=0, pady=5)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, border=0)
right_btn.grid(row=1, column=1, pady=5)

window.mainloop()
```

### Step 2: Create New Flash Cards
1. Read the data from the french_words.cvs file in the data folder
2. Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display
3. Use the pandas library to access the CSV file and generate a data frame. To get all the words/translation rows out as a list of dictionaries e.g. [{french_word: english_word}, {french_word2: english_word2}, {french_word3: english_word3}], use `DataFrame.to_dict(orient="records")`
```py
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
# 1. Read the data from the french_words.cvs file in the data folder
# 2. Pick a random French word/translation and put the word into the flashcard. Every time you press
#    the ❌ or ✅ buttons, it should generate a new random word to display
# 3. Use the pandas library to access the CSV file and generate a data frame. To get all
#    the words/translation rows out as a list of dictionaries
data_frame = pandas.read_csv("./data/french_words.csv")
data_dict = data_frame.to_dict(orient="records")
# print(data_dict)

def generate_word():
  word = random.choice(data_dict)
  canvas.itemconfig(foreign, text=word["French"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 265, image=front_card_img)
# Card text
canvas.create_text(400, 160, text="French", fill="black", font=LANGUAGE_FONT)
foreign = canvas.create_text(400, 280, text=data_dict[0]["French"], fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, borderwidth=0, highlightthickness=0, command=generate_word)
wrong_btn.grid(row=1, column=0, pady=5)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, border=0, command=generate_word)
right_btn.grid(row=1, column=1, pady=5)

window.mainloop()
```