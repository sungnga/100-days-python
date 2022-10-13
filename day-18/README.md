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
from turtle import Turtle, Screen, colormode
from random import randrange

turtle = Turtle()
turtle.shape("turtle")
colormode(255)


def change_color():
	r = randrange(0, 256)
	g = randrange(0, 256)
	b = randrange(0, 256)
	turtle.color((r, g, b))


def draw_shape(num_sides):
	degree = 360/num_sides
	for _ in range(num_sides):
		turtle.forward(100)
		turtle.right(degree)


shape_side = 3
while shape_side < 11:
	change_color()
	draw_shape(shape_side)
	shape_side += 1

screen = Screen()
screen.exitonclick()
```

#### Turtle challenge 4 - generate a random walk
```py
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
colormode(255)
turtle.width(5)
turtle.speed("fast")
directions = [0, 90, 180, 270]


def change_color():
	r = random.randrange(0, 256)
	g = random.randrange(0, 256)
	b = random.randrange(0, 256)
	turtle.color((r, g, b))


for _ in range(150):
	change_color()
	direction = random.choice(directions)
	turtle.forward(25)
	turtle.setheading(direction)

screen = Screen()
screen.exitonclick()
```

#### Python tuples and how to generate random RGB colors
- A tuple is a data type in Python
- Denoted by a pair of parenthesis: `(item1, item2, item3)`
- Similar to a Python list, each item in a tuple is **ordered**
- Unlike a list, a tuple is **immutable**
- If you want to change the items inside a tuple, put the tuple in a list
  ```py
  my_tuple = (5, 8, 1)
  list[my_tuple] #[5, 8, 1]
  ```
- To access items in a tuple, use the square bracket `[]` notation
  ```py
  my_tuple = (5, 8, 1)
  my_tuple[2] #accessing third item
  ```

#### Turtle challenge 5 - draw a spirograph


#### The Hirst Painting project part 1 - how to extract RGB values from images


####  The Hirst Painting project part 2 - drawing the dots