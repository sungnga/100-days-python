from tkinter import *


def miles_to_km():
  miles = float(miles_input.get())
  to_km = round(miles * 1.609, 2)
  result_label.config(text=f"{to_km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(row=1, column=2)

calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(row=2, column=1)

window.mainloop()
