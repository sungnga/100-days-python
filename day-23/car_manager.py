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
