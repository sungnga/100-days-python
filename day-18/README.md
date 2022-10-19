# DAY 18 - Turtle Graphics, Tuples, and Importing Modules

### Today's lessons:
- Turtle graphics - working with turtle module
- Tuples
- Importing modules, installing packages, and working with aliases

### Understanding Turtle graphics and how to use the documentation
- Turtle graphics docs: https://docs.python.org/3/library/turtle.html
- The turtle module comes with the Python standard library. No need to install

### Turtle challenge 1 - draw a square
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

### Importing modules, installing packages, and working with aliases
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
  - This is the place where we go find a module we want to use in our project and install it
- **Installing a Python package in PyCharm:**
  - In PyCharm, type `CMND + ,` to open the Preferences dialogue window
  - Select the current project folder and select Python Interpreter
  - Click on the "+" button to install a new Python package
  - Search for the package name and then click on the Install Package button to install it

### Turtle challenge 2 - draw a dashed line
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

### Turtle challenge 3 - drawing different shapes
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

### Turtle challenge 4 - generate a random walk
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

### Python tuples and how to generate random RGB colors
- A tuple is a data type in Python
- Denoted by a pair of parenthesis: `(item1, item2, item3)`
- Similar to a Python list, each item in a tuple is **ordered**
- Unlike a list, a tuple is **immutable**
- If you want to mutate the tuple, put the tuple in a list first
  ```py
  my_tuple = (5, 8, 1)
  my_list = [my_tuple]
  my_list[0] = (111, 3, "hello")

  print(my_list)  # [(111, 3, 'hello')]
  ```
- To access items in a tuple, use the square bracket `[]` notation
  ```py
  my_tuple = (5, 8, 1)
  my_tuple[2]  # accessing third item
  ```
- Generate random RGB colors
  ```py
  import random
  from turtle import Turtle, Screen, colormode
  import random

  turtle = Turtle()
  colormode(255)

  def change_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

  turtle.color(change_color())
  ```

### Turtle challenge 5 - draw a spirograph
```py
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
colormode(255)
turtle.width(1)
turtle.speed("fastest")


def change_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color


angle = 5
for _ in range(0, 360, angle):
  turtle.color(change_color())
  turtle.circle(100)
  turtle.right(angle)

screen = Screen()
screen.exitonclick()
```

### The Hirst Painting project part 1 - how to extract RGB values from images
- colorgram.py docs: https://pypi.org/project/colorgram.py/
- **Install the colorgram.py package**
  - In PyCharm, type `CMND + ,` to open the Preferences dialogue window
  - Select the current project folder and select Python Interpreter
  - Click on the "+" button to install a new Python package
  - Search for colorgram.py and click on the Install Package button
- File: main.py

  - Import the colorgram package
  - Find a Hirst painting on the web and import the image file to the project folder

  ```py
  import colorgram

  colors = colorgram.extract('hirst_image.jpg', 20)
  color_list = []

  for color in colors:
    color_list.append(tuple(color.rgb))

  print(colors)
  print(color_list)
  ```

### The Hirst Painting project part 2 - drawing the dots
- After we get the list of colors and printed to the console, copy and save the color list to a variable. Now we can just comment out the colorgram color extraction
- Create a Hirst dot painting of 10X10 dot grid. Each dot color is randomly chosen from the list of colors
- File: main.py
  ```py
  import turtle as t
  import random

  tom = t.Turtle()
  t.colormode(255)
  tom.hideturtle()
  tom.penup()
  tom.speed("fast")

  color_list = [(215, 159, 94), (166, 97, 51), (242, 236, 239), (225, 238, 233), (120, 169, 186),
                (29, 111, 146), (225, 199, 107), (33, 126, 93), (178, 10, 19), (199, 147, 35),
                (171, 57, 93), (217, 82, 102), (186, 17, 11), (5, 64, 31), (140, 184, 170), (6, 99, 69),
                (79, 76, 20), (162, 209, 199)]

  # for i in range(10):
  #   tom.goto(-220, -220 + (i * 50))
  #   for _ in range(10):
  #     tom.dot(20, random.choice(color_list))
  #     tom.forward(50)

  for i in range(100):
    if i % 10 == 0:
      tom.goto(-220, -220 + (i * 5))
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

  screen = t.Screen()
  screen.exitonclick()
  ```
