from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snaky = Snake()
food = Food()
scoreboard = Scoreboard()

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
  time.sleep(.4)
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
  for segment in snaky.segments[1:]:
    # If head collides with any segment in the tail
    if snaky.head.distance(segment) < 10:
      # Trigger game_over
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()