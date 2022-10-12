# DAY 18 - Turtle Graphics, Tuples, and Importing Modules

#### Today's lessons:
- Turtle graphics
- Tuples
- Importing modules, installing packages, and working with aliases 

#### Understanding Turtle graphics and how to use the documentation
- Turtle graphics docs: https://docs.python.org/3/library/turtle.html

#### Turtle challenge 1 - draw a square
```py
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("purple")

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)

for _ in range(4):
	turtle.forward(100)
	turtle.right(90)

screen = Screen()
screen.exitonclick()
```

#### Importing modules, installing packages, and working with aliases
- **Basic import**
  - `import <module_name>`
  - Example: `import turtle`
  ```py
  # Create a turtle object from the Turtle class
  import turtle

  turtle = turtle.Turtle()
  ```
- **from...import...**
  - `from <module_name> import <thing_in_module>`
  - Example: `from turtle import Turtle`
  - This is useful when we have many things in the module we want to use
  ```py
  # Create multiple object from Turtle class
  from turtle import Turtle, Screen

  tim = Turtle()
  tom = Turtle()
  terry = Turtle()

  screen = Screen()
  ```
- **Aliasing modules**
  - `import <module_name> as <alias_name>`
  - Example: `import turtle as t`
  - This is useful when a module name is very long
  ```py
  # Aliasing the turtle module
  import turtle as t

  tim = t.Turtle()
  ```
- **Installing modules**
  - Some built-in modules such as turtle and random are packaged with the Python standard library
  - The Python packages website: www.pypi.org
  - This is the place we go find a module we want to use in our project and install it

#### Turtle challenge 2 - draw a dashed line
```py
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("purple")

for _ in range(15):
	turtle.forward(10)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

screen = Screen()
screen.exitonclick()
```

#### Turtle challenge 3 - drawing different shapes
```py

```

#### Turtle challenge 4 - generate a random walk


#### Python tuples and how to generate random RGB colors


#### Turtle challenge 5 - draw a spirograph


#### The Hirst Painting project part 1 - how to extract RGB values from images


####  The Hirst Painting project part 2 - drawing the dots