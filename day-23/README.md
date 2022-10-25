# DAY 23 - The Turtle Crossing Capstone Project

### Step to building the Turtle Crossing Game:
- Setup screen
- Create and move cars
- Create player and move with key press
- Keeping score
- Detect collision with car
- Keeping score and changing car speed

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

### Create player and move with key press
- File: player.py
  ```py
  from turtle import Turtle

  STARTING_POSITION = (0, -200)
  MOVE_DISTANCE = 10
  FINISH_LINE_Y = 280


  class Player(Turtle):
    def __init__(self):
      super().__init__()
      self.shape('turtle')
      self.penup()
      self.goto(STARTING_POSITION)
      self.setheading(90)

    def move(self):
      self.forward(MOVE_DISTANCE)
      if self.ycor() >= FINISH_LINE_Y:
        self.goto(STARTING_POSITION)
  ```
- File: main.py
  ```py
  from turtle import Screen
  from player import Player

  screen = Screen()
  screen.setup(width=600, height=600)
  screen.tracer(0)

  player = Player()

  screen.listen()
  screen.onkeypress(key="Up", fun=player.move)
  ```

### Keeping score
- File: scoreboard.py
  - The scoreboard will display that the upper right corner of the screen
  ```py
  from turtle import Turtle

  FONT = ('Courier', 24, 'normal')


  class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.hideturtle()
      self.level = 0
      self.update_level()

    def update_level(self):
      self.clear()
      self.goto(-280, 260)
      self.write(f'Level: {self.level}', align='left', font=FONT)
  ```
- File: main.py
  - Import the Scoreboard class from scoreboard.py file
  - Instantiate a scoreboard object from the Scoreboard class
  ```py
  from scoreboard import Scoreboard

  scoreboard = Scoreboard()
  ```

### Detect collision and game over
- File: scoreboard.py
  - Inside the Scoreboard class, write a game_over method that displays the text "GAME OVER" in the center of the screen when the player collides with a car
  ```py
  def game_over(self):
    self.goto(0, 0)
    self.write('GAME OVER', align='center', font=FONT)
  ```
- File: main.py
  - If the player collides with a car, call the game_over() method on scoreboard to display the "GAME OVER" text and stop the game by setting the game_is_on to false
  ```py
  from scoreboard import Scoreboard

  scoreboard = Scoreboard()

  game_is_on = True
  while game_is_on:
    time.sleep(.3)
    screen.update()

    for car in cars:
      car.move()
      car.restart()

    # Detect collision with car
    for car in cars:
      if car.distance(player) <= 20:
        scoreboard.game_over()
        game_is_on = False
  ```

### Keeping score and changing car speed
- If the player successfully crossing to the other side, return to its original position, increase level on scoreboard, and increase car speed
- File: player.py
  - Write an is_at_finish_line method that if the player reaches the finish line, return player to original position and return true
  ```py
  def is_at_finish_line(self):
    if self.ycor() >= FINISH_LINE_Y:
      self.goto(STARTING_POSITION)
      return True
  ```
- File: car_manager.py
  - Create an attribute called move_speed and set it to .2 millisecond
  - Create a method called increase_speed that increases speed by .9 millisecond
  ```py
  from turtle import Turtle
  import random

  COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
  MOVE_INCREMENT = 10


  class CarManager(Turtle):
    def __init__(self, x, y):
      super().__init__()
      self.shape('square')
      self.turtlesize(stretch_wid=1, stretch_len=2)
      self.color(random.choice(COLORS))
      self.penup()
      self.goto(x, y)
      self.move_speed = .2

    def move(self):
      self.backward(MOVE_INCREMENT)

    def increase_speed(self):
      self.move_speed *= .9

    def restart(self):
      if self.xcor() < -300:
        self.setx(300)
        self.sety(random.randint(-250, 270))
  ```
- File: scoreboard.py
  - Write an increase_level method that increase the level attribute by 1 and update the scoreboard
  ```py
  def update_scoreboard(self):
    self.clear()
    self.goto(-280, 270)
    self.write(f'Level: {self.level}', align='left', font=FONT)

  def increase_level(self):
    self.level += 1
    self.update_scoreboard()
  ```
- File: main.py
  - In the time.sleep() method pass in the car's move_speed as an argument
  - Check if player has successfully crossing, up level in the scoreboard and increase car speed
  ```py
  game_is_on = True
  while game_is_on:
    time.sleep(cars[0].move_speed)
    screen.update()

    for car in cars:
      car.move()
      car.restart()

    # Detect collision with car
    for car in cars:
      if car.distance(player) <= 20:
        scoreboard.game_over()
        game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
      # Update scoreboard
      scoreboard.increase_level()
      # Increase car speed
      cars[0].increase_speed()
  ```
