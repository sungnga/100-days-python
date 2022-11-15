# DAY 28 - More Tkinter, Dynamic Typing, Pomodoro App

### Today's lessons:
- Building Pomodoro GUI application
- Dynamic typing

### Pomodoro App - Working with the Canvas widget and adding images to Tkinter
```py
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
```

### Pomodoro App - Complete the application's User Interface (UI)
```py
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"), pady=10)
timer_label.grid(row=0, column=1)

checkmark_label = Label(text="✓")
checkmark_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"), pady=10)
checkmark_label.grid(row=3, column=1)

start_btn = Button(text="Start")
start_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW)
reset_btn.grid(row=2, column=2)

window.mainloop()
```

### Pomodoro App - Add a count down mechanism
```py
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	count_down(14)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  # dynamic typing - changing from integer type to string type
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    # 1st arg is after a certain amount of time
    # 2nd arg is the function to call
    # 3rd+ args is any number of positional args you want to pass as input to the function call
    window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"), pady=10)
timer_label.grid(row=0, column=1)

checkmark_label = Label(text="✓")
checkmark_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"), pady=10)
checkmark_label.grid(row=3, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW)
reset_btn.grid(row=2, column=2)

window.mainloop()
```

### Pomodoro App - Dynamic typing


### Pomodoro App - Setting different timer sessions and values


### Pomodoro App - Adding checkmarks and resetting the application

