import turtle
import time

class FSM:
    def __init__(self):
        self.activeState = None
        self.handlers = {}
        self.state_stack =[]

    def push_state(self, name):
        self.state_stack.append(self.activeState)
        self.activeState = self.handlers[name]
        self.activeState()

    def pop_state(self):
        self.activeState = self.state_stack.pop()
        self.activeState()

    def add_state(self, name, handler):
        self.handlers[name] = handler

    def set_state(self, name):
        self.activeState = self.handlers[name]
        self.activeState()

    def update(self):
        if self.activeState is not None:
            self.activeState()


