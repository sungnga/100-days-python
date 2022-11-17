# DAY 29 - Password Manager GUI App with Tkinter

### Working with images and setting up the Canvas
```py
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(bg="white", fg="black", highlightthickness=0, width=39, insertbackground="black")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="W")
email_entry = Entry(bg="white", fg="black", insertbackground="black", highlightthickness=0, width=39)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="W")
email_entry.insert(0, "nga@example.com")
password_entry = Entry(bg="white", fg="black", insertbackground="black", highlightthickness=0, width=21)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons
generate_password_btn = Button(text="Generate Password", highlightbackground="white")
generate_password_btn.grid(row=3, column=2, sticky="W")
add_btn = Button(text="Add", highlightbackground="white", width=36)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
```

### Saving data to file
```py

```

### Dialog boxes and pop-ups in Tkinter
```py

```

### Generate a password and copy it to the clipboard
```py

```