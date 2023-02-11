import turtle
import time
import FSM
import math
from rabbit import Rabbit
from FSM import FSM
from PIL import Image
from Meat import Meat
import random


class TigerFMS:

    def __init__(self, rab):
        self.brain = FSM()
        self.brain.handlers = {
            "eat" : self.eat,
            "attack": self.attack,
            "hunting" : self.hunting,
            "jumping" : self.jumping,
            "walking": self.walk,
            "sleeping": self.sleeping
        }
        self.curr_time = time.time()
        self.tiger = turtle.Turtle()
        self.tiger.shape("tiger_resized.gif")
        self.tiger.penup()
        self.tiger.speed(0)
        self.tiger.setposition(-400, -300)
        self.tiger.speed(1)
        self.rabbit = rab
        self.brain.push_state("walking")


    def walk(self):
        print("walk")
        start_time = time.time()
        self.tiger.forward(20)
        if self.tiger.xcor() >= 400:
            self.tiger.left(180)

        elif self.tiger.xcor() <= -400:
            self.tiger.right(180)
        if ((self.tiger.xcor() - self.rabbit.rabbit.xcor())**2 + (self.tiger.ycor() - self.rabbit.rabbit.ycor())**2)**0.5 <= 200:
            self.brain.push_state("hunting")
        if start_time - self.curr_time >= 10:
            self.curr_time = time.time()
            self.brain.push_state("sleeping")
        self.brain.update()


    def eat(self):
        piece_meat = Meat(self.rabbit.rabbit.xcor(), self.rabbit.rabbit.ycor())
        self.rabbit.rabbit.hideturtle()

        while piece_meat.meat.health != 0:
            piece_meat.meat.health -= 1
            print("eat")
            time.sleep(0.2)
        piece_meat.meat.hideturtle()
        self.rabbit = Rabbit()
        self.rabbit.rabbit.setposition(random.randint(-400, 400), -300)




    def hunting(self):
        self.tiger.forward(5)
        distance = ((self.tiger.xcor() - self.rabbit.rabbit.xcor())**2 + (self.tiger.ycor() - self.rabbit.rabbit.ycor())**2)**0.5
        if distance > 200:
            self.brain.pop_state()

        if distance >= 150:
            self.brain.push_state("jumping")
            self.brain.pop_state()
        if distance <= 70 and self.rabbit.rabbit.health == 0:
            self.brain.push_state("eat")
            self.brain.pop_state()
        elif distance <= 50:
            self.brain.push_state("attack")
            self.brain.pop_state()
        self.brain.update()

    def attack(self):
        while self.rabbit.rabbit.health != 0:
            self.rabbit.rabbit.health -= 1
            print("bite")
            time.sleep(0.1)

    def jumping(self):
        print("jump")
        speed = 30
        alpha = 0.5
        g = 9.8
        start_x = self.tiger.xcor()
        start_y = self.tiger.ycor()
        for t in range(1, 11):
            if self.tiger.heading() == 180:
                x = start_x - ((start_x + 100) - start_x) * t / 10
                y = start_y + 30 * (-4 * (t / 10) ** 2 + 4 * (t / 10))
            else:
                x = start_x + ((start_x + 100) - start_x) * t / 10
                y = start_y + 30 * (-4 * (t / 10) ** 2 + 4 * (t / 10))
            self.tiger.goto(x, y)
        self.brain.pop_state()

    def sleeping(self):
        self.tiger.shape("tigerS_resized.gif")
        print("sleeping")
        time.sleep(2)
        self.tiger.shape("tiger_resized.gif")
        self.brain.pop_state()
