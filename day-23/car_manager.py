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
