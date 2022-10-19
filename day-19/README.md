# DAY 19 - Instances, State, and Higher Order Functions

### Today's lessons:
- More Turtle graphics
- Higher order functions
- Event listeners
- Object state and instances

### Python higher order functions & event listeners
- Event listeners are code that listen for what the user does. For example, a user might press a certain key or click on something to trigger a particular event
  ```py
  from turtle import Turtle, Screen

  tim = Turtle()
  screen = Screen()


  def move_forward():
    tim.forward(10)


  screen.listen()  # listen for events
  # When space key is pressed, move forward by 10
  screen.onkey(key="space", fun=move_forward)  # passing function as input
  screen.exitonclick()
  ```
- **Functions as inputs**
  - Passing a function into another function as input
  - NOTE that when passing a function as an input, we don't add parenthesis `()` after the function name
  ```py
  def function_a(something):
    #Do this with something
    #Then do this
    #Finally do this

  def function_b():
    #Do this

  function_a(function_b)
  ```
- **Higher order functions**
  - The idea of a higher order function is a function that can work with other functions
  - The higher order function takes other functions as inputs and work with it inside the body
  ```py
  # Add
  def add(n1, n2):
    return n1 + n2

  # Subtract
  def subtract(n1, n2):
    return n1 - n2

  # Multiply
  def multiply(n1, n2):
    return n1 * n2

  # Divide
  def divide(n1, n2):
    return n1 / n2

  # Higher order function
  def calculator(n1, n2, func):
    return func(n1, n2)

  result = calculator(2, 3, add)
  print(result)  #5
  ```

### Challenge: Make an Etch-A-Sketch app
```py
# W = Forwards
# S = Backwards
# A = Counter-clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def forward():
  tom.forward(10)


def backward():
  tom.backward(10)


def turn_left():
  tom.left(10)
  # tom.forward(3)


def turn_right():
  tom.right(10)
  # tom.forward(3)


def clear():
  tom.reset()


screen.listen()
screen.onkeypress(key='w', fun=forward)
screen.onkeypress(key='s', fun=backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
```

### Object state and instances
- Even though multiple objects can be constructed from the same class, they function completely independent of each other. Each object is also known as an **instance**
- Each object could have different attributes and perform different methods. In programming, is known as their **state**. You can have separate versions of the same object, each with a different state, and acting independently from each other

### Day 19 project: Turtle Racing Game
```py
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x_coord = -230
y_coord = -100
all_turtles = []

# Create 6 turtle instances
for i in range(6):
  new_turtle = Turtle(shape='turtle')
  new_turtle.penup()
  new_turtle.color(colors[i])
  new_turtle.goto(x=x_coord, y=y_coord)
  all_turtles.append(new_turtle)
  y_coord += 30

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_turtle = turtle.pencolor()
      if winning_turtle == user_bet:
        print(f"You've won! The {winning_turtle} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_turtle} turtle is the winner!")

    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)

screen.exitonclick()
```
