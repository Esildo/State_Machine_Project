import turtle
import time

class FSM:
    def __init__(self):
        self.activeState = None
        self.handlers = {}
        self.state_stack =[]

    def push_state (self,state)
        self.state_stack.

        
    def add_state(self, name, handler):
        self.handlers[name] = handler

    def set_state(self, name):
        self.activeState = self.handlers[name]
        self.activeState()

    def update(self):
        if self.activeState is not None:
            self.activeState()


