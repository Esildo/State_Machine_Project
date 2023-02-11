import turtle
import time
import FSM
from FSM import FSM

class TigerFMS:
    def __init__(self):
        self.brain = FSM()
        self.brain.handlers = {
            "walking": self.walk,
            "sleeping": self.sleeping
        }
        self.curr_time = time.time()

        self.tiger = turtle.Turtle()
        self.tiger.penup()
        self.tiger.color("orange")
        self.tiger.setposition(-400, -300)
        self.tiger.speed(0)
        self.tiger.speed(10)
        self.brain.set_state("walking")

    def walk(self):
        start_time = time.time()
        self.tiger.forward(20)
        if self.tiger.xcor() == 400:
            self.tiger.left(180)
        elif self.tiger.xcor() == -400:
            self.tiger.right(180)
        if start_time - self.curr_time >= 10:
            self.curr_time = time.time()
            self.brain.set_state("sleeping")
        self.brain.update()

    def sleeping(self):
        print("sleeping")
        time.sleep(2)
        self.brain.set_state("walking")
