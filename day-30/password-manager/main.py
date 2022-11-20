from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# 1. Create a function called generate_password()
# 2. When the Generate Password button is clicked, insert the generated password to the Password input field
# 3. Copy the generated password to the clipboard
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  letters_list = [choice(letters) for _ in range(randint(8, 10))]
  symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
  numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = letters_list + symbols_list + numbers_list

  shuffle(password_list)
  password = ''.join(password_list)
  if len(password_entry.get()) == 0:
    password_entry.insert(0, password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# 1. Create a function called save_data()
# 2. Write to the data inside the entries to a data.txt file when the Add button is clicked
# 3. Each website, email, and password combination should be on a new line inside the file
# 4. All fields need to be cleared after Add button is pressed
# 5. Do not save the data and show the pop up above if the website or password fields were left empty
def save_data():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  if website == "" or password == "":
    messagebox.showerror(
      title="Oops", message="Please don't leave any fields empty!")
  else:
    # TODO: Modify the code to handle the FileNotFoundError
    # Create a new data.json file if it does not exist
    # If the file already exists, then simply add the new entry
    try:
      with open("data.json", "r") as data_file:
        # Reading old data
        data = json.load(data_file)
    except FileNotFoundError:
      with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=2)
    else:
      # Updating old data with new data
      data.update(new_data)

      # Saving updated data
      with open("data.json", "w") as data_file:
        # 1st arg is the data to write
        # 2nd arg is the file to write to
        # 3rd arg is formatting the json data
        json.dump(data, data_file, indent=2)
    finally:
      website_entry.delete(0, END)
      website_entry.focus()
      password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
# 1. Add a "Search" button next to the website entry field
# 2. Adjust the layout and the other widgets as needed to get the desired look
# 3. Create a function called find_password() that gets triggered when the "Search" button is pressed
# 4. Check if the user's text entry matches an item in the data.json
# 5. If yes, show a messagebox with the website's name and password
# 6. Catch an exception that might occur trying to access the data.json show a messagebox with the text:
#    "No Data File Found"
# 7. If the user's website does not exist inside the data.json, show a messagebox that reads
#    "No details for the website exists"
def find_password():
  website = website_entry.get()
  try:
    with open("data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showerror(title="Error", message="No Data File Found")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=website.title(),
                          message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showerror(
        title="Not Found", message=f"No details for the {website} exists.")
  finally:
    website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(row=2, column=0, padx=15)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(bg="white", fg="black",
                      highlightthickness=0, width=21, insertbackground="black")
website_entry.grid(row=1, column=1, pady=5, sticky="W")
website_entry.focus()

email_entry = Entry(bg="white", fg="black",
                    insertbackground="black", highlightthickness=0, width=39)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="W")
email_entry.insert(0, "nga@example.com")

password_entry = Entry(bg="white", fg="black",
                       insertbackground="black", highlightthickness=0, width=21)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons
generate_password_btn = Button(
	text="Generate Password", highlightbackground="white", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="W")
add_btn = Button(text="Add", highlightbackground="white",
                 width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W")
search_btn = Button(text="Search", highlightbackground="white",
                    command=find_password, width=14)
search_btn.grid(row=1, column=2)

window.mainloop()
