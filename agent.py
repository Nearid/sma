from random import randint
from random import uniform
from pygame import Vector2

class Agent:
    def __init__(self, body):
        self.id = randint(1, 100000000)
        self.body = body
        self.perception = []

    def update(self):
        preys, dangers = self.filtrePerception()
        if len(preys) == 0 and len(dangers) == 0:
            self.body.acc = Vector2(uniform(-1, 1), uniform(-1, 1))

        if len(dangers) > 0:
            danger = dangers[0]
            if isinstance(danger, Agent):
                self.body.acc = self.body.pos - danger.body.pos
            else:
                self.body.acc = self.body.pos - danger.pos

        elif len(preys) > 0:
            prey = preys[0]

            if isinstance(prey, Agent):
                self.body.acc = prey.body.pos - self.body.pos
            else:
                self.body.acc = prey.pos - self.body.pos

    def show(self):
        self.body.show()

    def filtrePerception(self):
        pass


