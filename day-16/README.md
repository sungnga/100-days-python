# DAY 16 - Object Oriented Programming (OOP)

### Today's lessons:
- Object Oriented Programming (OOP)
- How to use OOP: classes and objects
- Constructing objects and accessing their attributes and methods
- How to add Python packages

### Why do we need OOP and how does it work?
- **Procedural programming:**
  - Set up procedures or functions that do particular thing. One procedure leads to another procedure. The computer is working from top to bottom and jumping into a function as needed
  - Procedural programming is one of the earliest days of programming. Older programming languages such as Fortran and Cobol rely on procedural programming
- **Object Oriented Programming (OOP):**
  - Object Oriented Programming paradigm comes in handy for a large and complex software project
  - Split large tasks into smaller modules that can be worked on by different people and can be reusable

### How to use OOP: classes and objects
- Object Oriented Programming (OOP) tries to model real-life objects
- An **object** has two things:
  - What it has. In programming is called **attributes**
    - Usually modeled with variables
  - What it does. In programming is called **methods**
    - Modeled by functions
- These variables and functions are not free floating, but they are associated with the object
- An object is a way of combining some piece of data and some functionality
- **Classes:**
  - A class is like the blueprint. It may contain attributes and methods
- **Objects:**
  - An object is an instance that is generated from a particular class
  - Multiple objects can be generated from a class

### Constructing objects and accessing their attributes and methods
- **Constructing objects:**
  - To construct an object from a class, simply add parenthesis `()` after the class name. This activates the construction of the object from the blueprint. Then assign the new object a name
  - The name of a class is usually written with the first letter of each word capitalized. This differentiates a class name from a variable or a function that we name
  - `car = CarBlueprint()`
- **Accessing object attributes and methods:**
  - An object has attributes and methods. To access them, simply add a period `.` after the object name followed by the name of the attribute or method. Similar to invoking a function, add the parenthesis `()` after the method name to invoke the method
  ```py
  car = carBlueprint()
  car.speed #get the speed attribute
  car.stop() #invoking the stop method on car object
  ```

### How to add Python packages and use PyPi
- Python Package Index: www.pypi.org
- The Python Package Index (PyPI) is a repository of software for the Python programming language developed and shared by the Python community
- **How to install and use a Python package:**
  - Go to PyPI website and search for the package you want to install. Can also view the package docs here. Copy the name of the Python package
  - PyCharm IDE, click on the Settings icon and select Preferences or press `CMND,`
  - In the Preferences window, select the current project from menu. And then select Python Interpreter
  - Click on the add `+` icon to install a package to the project. Paste the name of the Python package and click on Install Package
  - Once the package is installed, it'll show up in the Python Interpreter's list of installed packages
  - Now we can use the package by importing the module in our code file

### Practice modifying object attributes and calling methods
- Install the prettyTable Python package from pypi.org website
  ```py
  from prettytable import PrettyTable

  # Instantiate a table object from PrettyTable class
  table = PrettyTable()
  # Add a column by calling the .add_column() method
  table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
  table.add_column("Type", ["Electric", "Water", "File"])
  # Accessing the align attribute and modify its value. Align column to left
  table.align = "l"

  print(table)
  ```

### Day 16 project: The Coffee Machine in OOP
```py
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
  choice = input(f"What would you like? ({menu.get_items()}): ")
  menu_items = menu.get_items()

  if choice == "off":
    machine_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  elif choice in menu_items:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
  else:
    print("Invalid input. Please try again.")
```
