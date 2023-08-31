from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.random_car()



    def random_car(self):
        self.goto(300, random.randint(-250, 250))
        self.color(random.choice(COLORS))

    def move_car(self):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + self.speed)
        self.setx(new_x)


