# DAY 20-21 - Snake Game

#### 7 steps to building the Snake Game:
- Create a snake body
- Move the snake
- Create snake food
- Detect collision with food
- Create a scoreboard
- Detect collision with wall
- Detect collision with tail

#### Step 1: Create a snake body
```py
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Create a snake body
# Three square blocks
segments = []
x_coord = 0
y_coord = 0
for i in range(3):
  new_segment = Turtle(shape='square')
  new_segment.penup()
  new_segment.color('white')
  new_segment.goto(x=x_coord, y=y_coord)
  x_coord -= 20
  segments.append(new_segment)

screen.exitonclick()
```

#### Step 2: Move the snake
```py
import time

screen.tracer(0)

# Move the snake
game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(.1)
  # Move the last segment to second to last segment and so on
  # seg_num starts at last segment
  for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
	segments[0].forward(20)
```

#### Refactor code: Create a Snake class and move method to OOP
- At the end of the project we will have three classes: Snake, Food, and Scoreboard
- File: snake.py
  - Create a Snake class that constructs the snake body and has a move() method
  ```py
  from turtle import Turtle

  STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
  MOVE_DISTANCE = 20


  class Snake:
    def __init__(self):
      self.segments = []
      self.create_snake()

    def create_snake(self):
      for position in STARTING_POSITIONS:
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
      # Move the last segment to second to last segment and so on
      # seg_num starts at last segment
      for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
      self.segments[0].forward(MOVE_DISTANCE)
  ```
- File: main.py
  - Import the Snake class from snake.py file
  - Instantiate a snake object from the Snake class
  - Move the snake by calling the move() method
  ```py
  from turtle import Screen
  from snake import Snake
  import time

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor('black')
  screen.title('Snake Game')
  screen.tracer(0)

  snaky = Snake()

  # Move the snake
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.1)

    snaky.move()

  screen.exitonclick()
  ```

#### Step 3: Control the snake
- File: snake.py
  - Create a `head` attribute in the Snake class. This tells the direction the head of the snake is heading
  - One rule of the Snake Game is it cannot go back on itself. For example, if it's heading up, it cannot head down. If it's heading left, it cannot head right
  ```py
  from turtle import Turtle

  STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
  MOVE_DISTANCE = 20
  UP = 90
  LEFT = 180
  DOWN = 270
  RIGHT = 0


  class Snake:
    def __init__(self):
      self.segments = []
      self.create_snake()
      self.head = self.segments[0]

    def create_snake(self):
      for position in STARTING_POSITIONS:
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
      # Move the last segment to second to last segment and so on
      # seg_num starts at last segment
      for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
      self.head.forward(MOVE_DISTANCE)

    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)

    def down(self):
      if self.head.heading() != UP:
        self.head.setheading(DOWN)

    def left(self):
      if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

    def right(self):
      if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
  ```
- File: main.py
  - We control the snake by using the Up, Down, Left, and Right arrow keys
  - Use key binding to bind the function to a particular key press
  ```py
  from turtle import Screen
  from snake import Snake
  import time

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor('black')
  screen.title('Snake Game')
  screen.tracer(0)

  snaky = Snake()

  screen.listen()
  screen.onkey(fun=snaky.up, key='Up')
  screen.onkey(fun=snaky.down, key='Down')
  screen.onkey(fun=snaky.left, key='Left')
  screen.onkey(fun=snaky.right, key='Right')
  screen.onkey(fun=snaky.stop, key='space')

  # Move the snake
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.1)

    snaky.move()

  screen.exitonclick()
  ```