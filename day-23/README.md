# DAY 23 - The Turtle Crossing Capstone Project

### Step to building the Turtle Crossing Game:
- Setup screen
- Create and move cars

### Setup screen
- File: main.py
  ```py
  from turtle import Screen

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.tracer(0)

  game_is_on = True
  while game_is_on:
    time.sleep(.1)
    screen.update()

  screen.exitonclick()
  ```

### Create and move cars
- File: main.py
  ```py
  from turtle import Screen
  from player import Player
  from car_manager import CarManager
  from scoreboard import Scoreboard
  import time
  import random

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.tracer(0)

  cars = []
  for i in range(5):
    cars.append(CarManager())

  game_is_on = True
  while game_is_on:
    time.sleep(.1)
    screen.update()
    random.choice(cars).move()

  screen.exitonclick()
  ```
- File: car_manager.py
  ```py
  from turtle import Turtle
  import random

  COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
  STARTING_MOVE_DISTANCE = 5
  MOVE_INCREMENT = 10


  class CarManager(Turtle):
    def __init__(self):
      super().__init__()
      self.create_car()

    def create_car(self):
      self.shape('square')
      self.turtlesize(stretch_wid=1, stretch_len=2)
      self.color(random.choice(COLORS))
      self.penup()
      self.goto(300, random.randint(-290, 290))

    def move(self):
      self.backward(MOVE_INCREMENT)
  ```