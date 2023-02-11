import turtle
from FSM import FSM

class Rabbit:

    def __init__(self):
        self.brainR = FSM()
        self.rabbit = turtle.Turtle()
        self.rabbit.penup()
        self.rabbit.speed(0)
        self.rabbit.setposition(300, -300)
        self.rabbit.speed(1)
        self.rabbit.color("white")
        self.rabbit.shape("rabbit_resized.gif")
        self.rabbit.health = 3