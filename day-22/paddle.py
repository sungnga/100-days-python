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
