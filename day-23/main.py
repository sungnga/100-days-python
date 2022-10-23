from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random


def create_cars():
  for _ in range(25):
    random_x = random.randint(300, 1000)
    random_y = random.randint(-270, 270)
    cars.append(CarManager(random_x, random_y))


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = []
create_cars()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
  time.sleep(.3)
  screen.update()
  for car in cars:
    car.move()
    car.restart()

screen.exitonclick()
