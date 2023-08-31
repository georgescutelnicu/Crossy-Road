import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")


all_cars = []
game_is_on = True
count = 0
speed = 0



while game_is_on:
    time.sleep(0.1)
    screen.update()

    count += 1
    if count == 4:
        car = CarManager(speed)
        all_cars.append(car)
        count = 0
    for car in all_cars:
        car.move_car()
        if player.distance(car) < 27:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        scoreboard.new_level()
        player.sety(-280)
        speed += 10



screen.exitonclick()

