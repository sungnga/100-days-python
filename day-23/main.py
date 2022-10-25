from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random


def create_cars():
  for _ in range(25):
    random_x = random.randint(100, 1000)
    random_y = random.randint(-250, 270)
    cars.append(CarManager(random_x, random_y))


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []
create_cars()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

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

screen.exitonclick()
