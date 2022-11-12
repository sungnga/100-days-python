# DAY 27 - GUI with Tkinter and Function Arguments

### Today's lessons:
- Packing and unpacking functions in Python
- Creating desktop GUI apps with Tkinter
- Setting default values for optional arguments inside a function header
- *args - many positional arguments
- **kwargs: many keyword arguments

### Creating windows and labels with Tkinter
- Tkinter library is already pre-installed in Python
```py
import tkinter

# Create a window object from the Tk class
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# ----------CREATE COMPONENTS---------- #
# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "normal"))
# pack() method places the component onto the screen
my_label.pack()

# mainloop() method keeps the window on the screen and listens for user inputs
# This line must be at the very end of the program
window.mainloop()
```

### Setting default values for optional arguments inside a function header
- For functions with arguments with default values, it's optional to pass in the args when calling the function
```py
# Keyword arguments
def my_function(a, b, c):
  #Do this with a
  #Then do this with b
  #Finally do this with c

my_function(c=3, a=1, b=2)

# Arguments with default values
def my_function(a=1, b=2, c=3):
  #Do this with a
  #Then do this with b
  #Finally do this with c

# Changing the default value argument
# If we don't specify an argument, it'll take on its default value
my_function(b=5)
```

### *args: Many positional arguments
- Passing in `*args` as a parameter to a function will allow the function to accept any number of arguments when the function is called
- The `*args` is also known as the ***unlimited positional arguments*** because the position of the argument which is passed to the function matters
- The `*` operator collects all the arguments into a **tuple**
```py
def add(*args):
  print(type(args))  # is a tuple
  print(args[2])  # can access their values by their positions

  sum_total = 0
  for n in args:  # can loop through a tuple
    sum_total += n
  return sum_total

# This function can accepts many number of arguments
print(add(4, 8, 9))
```

### **kwargs: Many keyword arguments
- Passing in `**kwargs` as a parameter to a function will allow the function to accept ***unlimited number of keyword arguments***
- The `**` operator collects all the arguments into a **dictionary**
```py
def calculate(n, **kwargs):
  print(type(kwargs))  # is a dictionary
  print(kwargs)  # {'add': 3, 'multiply': 5}
  print(kwargs["add"])  # access the kwarg value by their key name

  for key, value in kwargs.items():
    print(key)
    print(value)
    
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)
	
# This function can take many keyword arguments
calculate(2, add=3, multiply=5)

# Create a class with many optional keyword arguments
class Car:
  def __init__(self, **kwargs):
    # The great thing about the .get() method is that it'll return None
    # if it cannot find the key name in kwargs
    self.make = kwargs.get("make")
    self.model = kwargs.get("model")
    self.color = kwargs.get("color")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
```

### Buttons, entry, setting component options
- Tkinter entry docs: http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
```py
from tkinter import *

# Create a window object from the Tk class
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# ----------CREATE COMPONENTS---------- #
# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "normal"))
# pack() method places the component onto the screen
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
  print("I got clicked")
  new_text = input.get() # takes the input from Entry
  my_label.config(text=new_text) # prints the input text as label when button is clicked

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
print(input.get())  # nothing gets printed

# mainloop() method keeps the window on the screen and listens for user inputs
# This line must be at the very end of the program
window.mainloop()
```

### Other Tkinter widgets: radiobuttons, scales, checkbuttons, and more
```py
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
  print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
  #gets the current value in spinbox.
  print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
  print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
  #Prints 1 if On button checked, otherwise 0.
  print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
  print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
  # Gets current selection from listbox
  print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
  listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```

### Tkinter layout managers: pack(), place() and grid()



### Day 27 project: Mile to Kilometers Converter