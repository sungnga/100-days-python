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


  def create_cars():
    for _ in range(30):
      random_x = random.randint(300, 1000)
      random_y = random.randint(-270, 270)
      cars.append(CarManager(random_x, random_y))


  cars = []
  create_cars()

  game_is_on = True
  while game_is_on:
    time.sleep(.2)
    screen.update()
    for car in cars:
      car.move()
      car.restart()

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
    def __init__(self, x, y):
      super().__init__()
      self.shape('square')
      self.turtlesize(stretch_wid=1, stretch_len=2)
      self.color(random.choice(COLORS))
      self.penup()
      self.goto(x, y)

    def move(self):
      new_x = self.xcor() - MOVE_INCREMENT
      self.goto(new_x, self.ycor())

    def restart(self):
      if self.xcor() < -300:
        self.setx(300)
        self.sety(random.randint(-270, 270))
  ```