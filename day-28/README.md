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
- Python is a strongly, dynamically typed language
- **Strong typing** means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't become an integer
- **Dynamic typing** means runtime objects (values) have a type, as opposed to static typing where variables have a type
- In Python, changing the type of a variable is possible. Other
  ```py
  user = 1
  user = "jane"
  ```

### Pomodoro App - Setting different timer sessions and values
- Set a `reps` variable as a global constant
- 1st rep: work 25 mins
- 2nd rep: break 5 mins
- 3rd rep: work 25 mins
- 4th rep: break 5 mins
- 5th rep: work 25 mins
- 6th rep: break 5 mins
- 7th rep: work 25 mins
- 8th rep: long break 30 mins
- In the count_down() method, when the `count` is equal to 0, we want to call the start_time() method again
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
  LONG_BREAK_MIN = 30
  reps = 0

  # ---------------------------- TIMER MECHANISM ------------------------------- # 
  def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps == 8:
      timer_label.config(text="Break", fg=RED)
      count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    elif reps in (2, 4, 6):
      timer_label.config(text="Break", fg=PINK)
      count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    elif reps in (1, 3, 5, 7):
      timer_label.config(text="Work", fg=GREEN)
      count_down(work_sec)


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
    else:
      start_timer()
  ```

### Pomodoro App - Adding checkmarks and resetting the application
- We add the checkmark for every two reps when a work is completed. We do this inside the count_down() method right after we called the start_timer() function
- To add the functionality to the Reset button, create a reset_timer() function. This function does the following:
  - To stop the running timer, we need to call the window.after_cancel() method and pass in the running timer. NOTE that the countdown timer method, window.after(), is called inside another method, we need to save it as a global variable before we can use it in this function
  - Reset the reps constant
  - Reset the checkmark_label to an empty string
  - Reset the timer_label text to "Timer" again
  - Reset the canvas countdown timer back to "00:00"
- Lastly, to link the reset_timer function to the Reset button, set the `command` option to reset_timer function but without calling it
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
  LONG_BREAK_MIN = 30
  reps = 0
  timer = None

  # ---------------------------- TIMER RESET ------------------------------- #
  def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    checkmark_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

  # ---------------------------- TIMER MECHANISM ------------------------------- # 
  def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    # If it's the 8th rep:
    if reps == 8:
      timer_label.config(text="Break", fg=RED)
      count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    elif reps in (2, 4, 6):
      timer_label.config(text="Break", fg=PINK)
      count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    elif reps in (1, 3, 5, 7):
      timer_label.config(text="Work", fg=GREEN)
      count_down(work_sec)


  # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
  def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # dynamic typing - changing from integer type to string type
    if count_sec < 10:
      count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
      global timer
      # 1st arg is after a certain amount of time
      # 2nd arg is the function to call
      # 3rd+ args is any number of positional args you want to pass as input to the function call
      timer = window.after(1000, count_down, count - 1)
    else:
      start_timer()
      check_marks = ""
      # reps/2 will return a floating number. We need to convert it to a whole number
      work_sessions = math.floor(reps/2)
      for _ in range(work_sessions):
        check_marks += "✓"
      checkmark_label.config(text=check_marks)


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

  checkmark_label = Label(text="")
  checkmark_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"), pady=10)
  checkmark_label.grid(row=3, column=1)

  start_btn = Button(text="Start", command=start_timer)
  start_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW)
  start_btn.grid(row=2, column=0)

  reset_btn = Button(text="Reset")
  reset_btn.config(font=(FONT_NAME, 20), highlightbackground=YELLOW, command=reset_timer)
  reset_btn.grid(row=2, column=2)

  window.mainloop()
  ```
