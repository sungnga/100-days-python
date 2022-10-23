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
