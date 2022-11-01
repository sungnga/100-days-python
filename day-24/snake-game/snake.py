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
      self.add_segment(position)

  def add_segment(self, position):
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    self.segments.append(new_segment)

  def reset_snake(self):
    for seg in self.segments:
      seg.reset()
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]

  def extend(self):
    # Get the position of the last segment
    # This is the position we use to add a new segment
    self.add_segment(self.segments[-1].position())

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

  def stop(self):
    self.head.forward(0)
