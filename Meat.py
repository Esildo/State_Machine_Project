import turtle
from FSM import FSM

class Meat:

    def __init__(self, x, y):
        self.brainR = FSM()
        self.meat = turtle.Turtle()
        self.meat.penup()
        self.meat.speed(0)
        self.meat.setposition(x, y)
        self.meat.color("white")
        self.meat.shape("meat_resized.gif")
        self.meat.health = 5