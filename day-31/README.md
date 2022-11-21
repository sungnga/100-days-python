# DAY 31 - Flash Card App Capstone Project

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

# Front Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 265, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

wrong_btn_img = PhotoImage(file="./images/wrong.png")
right_btn_img = PhotoImage(file="./images/right.png")

# Buttons
wrong_btn = Button(image=wrong_btn_img, borderwidth=0, highlightthickness=0)
wrong_btn.grid(row=1, column=0, pady=5)
right_btn = Button(image=right_btn_img, highlightthickness=0, border=0)
right_btn.grid(row=1, column=1, pady=5)

# Text
canvas.create_text(400, 150, text="french", fill="black", font=LANGUAGE_FONT)
canvas.create_text(400, 265, text="word", fill="black", font=WORD_FONT)

window.mainloop()
```