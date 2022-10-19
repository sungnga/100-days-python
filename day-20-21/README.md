# DAY 20-21 - Snake Game

### Today's lessons:
- More turtle graphics
  - update() method
- Class inheritance
- How to slice lists and tuples

### 7 steps to building the Snake Game:
- Create a snake body
- Move the snake
- Create snake food
- Detect collision with food
- Create a scoreboard
- Detect collision with wall
- Detect collision with tail

### Step 1: Create a snake body
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

### Step 2: Move the snake
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

### Refactor code: Create a Snake class and move method to OOP
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

### Step 3: Control the snake
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

### Class inheritance
- A class an inherit attributes and methods from another class. This is known as **class inheritance**. The class that other classes can inherit from (a parent class) is known as the **superclass**
- For example, a Fish class can inherit attributes and methods from an Animal class. The Animal class is the superclass. So a fish object that's constructed from the Fish class will inherit all the attributes and methods from the Animal class
- Class inheritance:
  ```py
  class Fish(Animal):
    def __init__(self):
      # Initializing super class
      super().__init__()
  ```
- Example of class inheritance:
  ```py
  class Animal:
    def __init__(self):
      self.num_eyes = 2

    def breathe(self):
      print('Inhale, exhale')

  class Fish(Animal):
    def __init__(self):
      super().__init__()

    # Modifying a method inherited from the superclass
    def breathe(self):
      # Get the functionality of the breathe() method from superclass
      super().breathe()
      # Add to the breathe() method from superclass
      print('doing this underwater.')

    def swim(self):
      print('moving in water.')

  nemo = Fish()
  nemo.swim()
  nemo.breathe()
  print(nemo.num_eyes)
  ```

### Step 4: Detect collision with food
- Create a Food class that inherits from the Turtle class
- Generate the food properties
- Create a food object from the Food class in main.py file and display it on screen
- Create a `refresh()` method on the Food class so the food will go to a random location
- Compare the distance between the snake head and the food. If they're less than 15, move the food to a new random location by calling the refresh() method
- File: food.py
  ```py
  from turtle import Turtle
  import random

  class Food(Turtle):
    def __init__(self):
      super().__init__()
      self.shape('circle')
      self.penup()
      self.shapesize(stretch_len=0.5, stretch_wid=0.5)
      self.color('magenta')
      self.speed('fastest')
      self.refresh()

    # Move food object to random location
    def refresh(self):
      random_x = random.randint(-280, 280)
      random_y = random.randint(-280, 280)
      self.goto(random_x, random_y)
  ```
- File: main.py
  - Import the Food class from
  ```py
  from turtle import Screen
  from snake import Snake
  from food import Food
  import time

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor('black')
  screen.title('Snake Game')
  screen.tracer(0)

  snaky = Snake()
  food = Food()

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

    # Detect collision with food
    if snaky.head.distance(food) < 15:
      food.refresh()

  screen.exitonclick()
  ```

### Step 5: Create a scoreboard and keep score
- File: scoreboard.py
  - Create a Scoreboard class that's inherited from the Turtle class
  - The Scoreboard class should have a method that increases the score by one point every time the snake head hits the food
  ```py
  from turtle import Turtle

  ALIGNMENT = 'center'
  FONT = ('Courier', 20, 'normal')


  class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.score = 0
      self.color('white')
      self.penup()
      self.goto(0, 270)
      self.hideturtle()
      self.update_scoreboard()

    def update_scoreboard(self):
      self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
      self.score += 1
      self.clear()
      self.update_scoreboard()
  ```
- File: main.py
  - Import the Scoreboard class
  - Call the .increase_score() method when the snake head hits the food
  ```py
  from scoreboard import Scoreboard

  scoreboard = Scoreboard()

  # Move the snake
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.1)
    snaky.move()

    # Detect collision with food
    if snaky.head.distance(food) < 15:
      food.refresh()
      scoreboard.increase_score()
  ```

### Step 6: Detect collision with wall
- The screen size is 600x600. The edge of each side of the screen is 300 at the top, 300 at the right, -300 at the bottom, and -300 at the left. If the snake head has gone pass this border, display a text to let the user know game over 
- File: scoreboard.py
  - In the Scoreboard class, write a game_over method that displays a text that says "GAME OVER". The text should be at the center of the screen
  ```py
  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
  ```
- File: main.py
  - Write an if statement that checks if the snake head has gone pass the screen border at 280, display the text "GAME OVER" and stop the game
  ```py
  # Move the snake
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.1)
    snaky.move()

    # Detect collision with food
    if snaky.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()

    # Detect collision with wall
    if snaky.head.xcor() > 280 or snaky.head.xcor() < -280 or snaky.head.ycor() > 280 or snaky.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()
  ```

### Step 7: Detect collision with tail
- When the snake hits the food, we need to add a segment to the snake tail. This way the snake will grow in length and we can start detecting the collision with its tail
- File: snake.py
  - Create an add_segment() method that creates a new_segment from the Turtle class and append it to the segments list
  - In the create_snake() method, loop through the positions in the STARTING_POSITION list, and for each position, call the add_segment() method and pass in the position as an argument
  - Create an extend() method that calls the add_segment() method to add a new_segment at the last segment's position (the end tail)
  ```py
  STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

  class Snake:
    def __init__(self):
      self.segments = []
      self.create_snake()
      self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self, position):
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    # Get the position of the last segment
    # This is the position we use to add a new segment
    self.add_segment(self.segments[-1].position())
  ```
- File: main.py
  - A snake segment is 20x20. To detect the collision with the tail, we loop through the snake segments. Check if the snake head distance to the segment is less than 10, the snake head has collided with its tail and trigger the game_over() method
  - Note that the first segment in the segments list is the snake head. We want to bypass the snake head
  ```py
  # Move the snake
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.1)
    snaky.move()

    # Detect collision with food
    if snaky.head.distance(food) < 15:
      food.refresh()
      snaky.extend()
      scoreboard.increase_score()

    # Detect collision with wall
    if snaky.head.xcor() > 280 or snaky.head.xcor() < -280 or snaky.head.ycor() > 280 or snaky.head.ycor() < -280:
      game_is_on = False
      scoreboard.game_over()

    # Detect collision with tail
    for segment in snaky.segments:
      # Bypassing the snake head
      if segment == snaky.head:
        pass
      # If head collides with any segment in the tail
      elif snaky.head.distance(segment) < 10:
        # Trigger game_over
        game_is_on = False
        scoreboard.game_over()
  ```

### How to slice lists and tuples and refactor Snake Game
- Slicing is getting a segment out of a list or tuple
- To slice a list or a tuple, use the square notation `[]` and the colon `:` to mark the beginning and end of the slice. This notation works exactly the same for both lists and tuples
  ```py
  piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

  # Slicing from position 2 to 5
  print(piano_keys[2:4])  #['c', 'd', 'e']

  # Slicing from position 2 to the end of list
  print(piano_keys[2:])  #['c', 'd', 'e', 'f', 'g']

  # Slicing from the beginning up to position 5
  print(piano_keys[:5])  #['a', 'b', 'c', 'd', 'e']

  # Specify a third number to set the increment
  # Skip every 2nd one
  print(piano_keys[2:5:2])  #['c', 'e']
  print(piano_keys[::2])  #['a', 'c', 'e', 'g']

  # Reverse the list
  print(piano_keys[::-1])  #['g', 'f', 'e', 'd', 'c', 'b', 'a']
  ```
- Refactor Snake Game using slicing
  ```py
  # Detect collision with tail
  # Slicing from 2nd segment to the end of segments list
  for segment in snaky.segments[1:]:
    # If head collides with any segment in the tail
    if snaky.head.distance(segment) < 10:
      # Trigger game_over
      game_is_on = False
      scoreboard.game_over()
  ```