# DAY 22 - The Pong Game

### Steps to building the Pong Game:
- Create the screen
- Create and move a paddle
- Create another paddle
- Create the ball and make it move
- Detect collision with wall and bounce
- Detect collision with paddle
- Detect when paddle misses
- Keep score
- Changing the ball speed

### Create the screen
- File: main.py
  ```py
  from turtle import Screen

  screen = Screen()
  screen.setup(width=800, height=600)
  screen.bgcolor('black')
  screen.title('Pong Game')
  screen.tracer(0)

  game_is_on = True
  while game_is_on:
    screen.update()

  screen.exitonclick()
  ```

### Create and move a paddle
- File: paddle.py
  ```py
  from turtle import Turtle


  class Paddle(Turtle):
    def __init__(self, position):
      super().__init__()
      self.shape('square')
      self.penup()
      self.goto(position)
      self.turtlesize(stretch_len=1, stretch_wid=5)
      self.color('white')

    def move_up(self):
      new_y = self.ycor() + 20
      if self.ycor() < 260:
        self.goto(self.xcor(), new_y)

    def move_down(self):
      new_y = self.ycor() - 20
      if self.ycor() > -260:
        self.goto(self.xcor(), new_y)
  ```
- File: main.py
  ```py
  from turtle import Screen
  from paddle import Paddle

  screen = Screen()
  screen.setup(width=800, height=600)
  screen.bgcolor('black')
  screen.title('Pong Game')
  screen.tracer(0)

  r_paddle = Paddle((350, 0))

  screen.listen()
  screen.onkeypress(key="Up", fun=r_paddle.move_up)
  screen.onkeypress(key="Down", fun=r_paddle.move_down)

  game_is_on = True
  while game_is_on:
    screen.update()

  screen.exitonclick()
  ```

### Create another paddle
- File: main.py
  ```py
  from turtle import Screen
  from paddle import Paddle

  screen = Screen()
  screen.setup(width=800, height=600)
  screen.bgcolor('black')
  screen.title('Pong Game')
  screen.tracer(0)

  r_paddle = Paddle((350, 0))
  l_paddle = Paddle((-350, 0))

  screen.listen()
  screen.onkeypress(key="Up", fun=r_paddle.move_up)
  screen.onkeypress(key="Down", fun=r_paddle.move_down)
  screen.onkeypress(key="e", fun=l_paddle.move_up)
  screen.onkeypress(key="d", fun=l_paddle.move_down)

  game_is_on = True
  while game_is_on:
    screen.update()

  screen.exitonclick()
  ```

### Create the ball and make it move
- File: ball.py
  ```py
  from turtle import Turtle


  class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.color('white')
      self.shape('circle')
      self.penup()

    def move(self):
      new_x = self.xcor() + 10
      new_y = self.ycor() + 10
      self.goto(new_x, new_y)
  ```
- File: main.py
  ```py
  from turtle import Screen, Turtle
  from paddle import Paddle
  from ball import Ball
  import random
  import time

  screen = Screen()
  screen.setup(width=800, height=600)
  screen.bgcolor('black')
  screen.title('Pong Game')
  screen.tracer(0)

  r_paddle = Paddle((350, 0))
  l_paddle = Paddle((-350, 0))

  ball = Ball()

  screen.listen()
  screen.onkeypress(key="Up", fun=r_paddle.move_up)
  screen.onkeypress(key="Down", fun=r_paddle.move_down)
  screen.onkeypress(key="e", fun=l_paddle.move_up)
  screen.onkeypress(key="d", fun=l_paddle.move_down)

  game_is_on = True
  while game_is_on:
    screen.update()
    ball.move()
    time.sleep(.1)

  screen.exitonclick()
  ```

### Detect collision with wall and bounce
- We only need to detect collision when the ball hits the top or bottom wall. If the ball hits the right or left side of the wall, it should be caught by one of the paddles
- If the paddle misses the ball, the opponent will score one point
- File: ball.py
  - Write a bounce method where the ball bounces the opposite in y-axis
  ```py
  from turtle import Turtle


  class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.color('white')
      self.shape('circle')
      self.penup()
      self.x_move = 10
      self.y_move = 10

    def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

    def bounce(self):
      self.y_move *= -1
  ```
- File: main.py
  - The screen is 600px tall. Detect collisions with the top and bottom walls. Change the ball's movement direction upon collision
  - When the ball hits the wall, call the bounce() method on the ball
  ```py
  game_is_on = True
  while game_is_on:
    screen.update()
    ball.move()
    time.sleep(.1)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      # Ball bounces
      ball.bounce()
  ```

### Detect collision with paddle
- When the ball hits the wall, we want the ball to move the opposite in y-axis
- When the ball hits a paddle, we want the ball to move the opposite in x-axis
- File: ball.py
  - Rename the bounce method to bounce_y. This method bounces in y-axis
  - Create a bounce_x method where the ball bounces the opposite in x-axis
  ```py
  from turtle import Turtle
  import random


  class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.color('white')
      self.shape('circle')
      self.penup()
      self.x_move = 10
      self.y_move = 10

    def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

    def bounce_y(self):
      self.y_move *= -1

    def bounce_x(self):
      self.x_move *= -1
  ```
- File: main.py
  - Detecting collision with the paddle can be a little tricky, because the measure distance of the paddle is from the center point. The paddle size is 20X100. Another way to detect a collision is to check if the ball has gone pass a certain point on the screen
  - Call the bounce_x() method if the ball collides with the left or right paddle
  ```py
  game_is_on = True
  while game_is_on:
    screen.update()
    ball.move()
    time.sleep(.1)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
      ball.bounce_x()
  ```

### Detect when paddle misses
- Detect if the ball goes out of bound at the edge of the screen. If yes, reset the ball's position to the center of the screen. The ball should then start moving towards the other player
- File: ball.py
  - Inside the Ball class, write a reset_position() method that sets the ball back to its original position at 0, 0 coordinate. Also make the ball to go reverse on its x-axis
  ```py
  def reset_position(self):
    self.goto(0, 0)
    self.bounce_x()
  ```
- File: main.py
  - Check if the r_paddle misses the ball, call the reset_position() method on ball
  - Do the same with the l_paddle
  ```py
  # Detect r_paddle misses
  if ball.xcor() > 380:
    ball.reset_position()

  # Detect l_paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
  ```

### Keep score
- File: scoreboard.py
  - Write a Scoreboard class that display the score for the left side and right side players. The Scoreboard class is a subclass of the Turtle class
  - Write two methods, one for each player, to increase a point for the player every time the opponent misses the ball and update the scoreboard
```py
from turtle import Turtle


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.l_score, align='center', font=('Courier', 70, 'normal'))
    self.goto(100, 200)
    self.write(self.r_score, align='center', font=('Courier', 70, 'normal'))

  def l_point(self):
    self.l_score += 1
    self.update_scoreboard()

  def r_point(self):
    self.r_score += 1
    self.update_scoreboard()
```
- File: main.py
  - Import the Scoreboard class and instantiate a scoreboard object
  - When a player misses the ball, increase a point for the opponent
  ```py
  from scoreboard import Scoreboard

  scoreboard = Scoreboard()

  game_is_on = True
  while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
      ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > 380:
      ball.reset_position()
      scoreboard.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -380:
      ball.reset_position()
      scoreboard.r_point()
  ```

### Changing the ball speed
- Let's make the game a little more challenging by increasing the ball speed every time it hits a paddle
- File: ball.py
  - In the Ball class, create an attribute called move_speed and initialize it to .1. The lower the number, the faster the ball moves
  - When the ball is moving in the opposite direction on the x-axis, this means it has hit a paddle. We increase the move_speed here
  - When a paddle misses the ball and the ball resets its position, we also want to reset the move_speed to its initial speed
  ```py
  from turtle import Turtle


  class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.color('white')
      self.shape('circle')
      self.penup()
      self.x_move = 10
      self.y_move = 10
      self.move_speed = .1

    def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

    def bounce_y(self):
      self.y_move *= -1

    def bounce_x(self):
      self.x_move *= -1
      self.move_speed *= .9

    def reset_position(self):
      self.goto(0, 0)
      self.move_speed = .1
      self.bounce_x()
  ```
- File: main.py
  - On the screen, the ball speed is controlled by the `time.sleep()` method. We pass our ball.move_speed value as an argument here
  ```py
  game_is_on = True
  while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
  ```