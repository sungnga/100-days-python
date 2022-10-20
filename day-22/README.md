# DAY 22 - The Pong Game

### Steps to building the Pong Game:
- Create the screen
- Create and move a paddle
- Create another paddle
- Create the ball and make it move
- Detect collision with wall and bounce
- Detect collision and paddle
- Detect when paddle misses
- Keep score

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
  - Write a bounce method where the ball bounces the opposite in y-direction
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
- When the ball hits the wall, we want the ball to move the opposite in y-direction
- When the ball hits a paddle, we want the ball to move the opposite in x-direction
- File: ball.py
  - Rename the bounce method to bounce_y. This method bounces in y-direction
  - Create a bounce_x method where the ball bounces the opposite in x-direction
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