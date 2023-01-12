from random import randint
from random import uniform

import core
from pygame import Vector2

class Agent:
    def __init__(self, body):
        self.id = randint(1, 100000000)
        self.body = body
        self.perception = []
        self.hunting = False

    def update(self):
        self.hunting = self.body.hunger[0] / self.body.hunger[1] > 0.5

        preys, dangers = self.filtrePerception()
        if len(preys) == 0 and len(dangers) == 0:
            self.body.acc = Vector2(uniform(-1, 1), uniform(-1, 1))

        if len(dangers) > 0:
            danger = dangers[0]
            if isinstance(danger, Agent):
                self.body.acc = self.body.pos - danger.body.pos
            else:
                self.body.acc = self.body.pos - danger.pos

        elif len(preys) > 0 and self.hunting:
            prey = preys[0]

            if isinstance(prey, Agent):
                self.body.acc = prey.body.pos - self.body.pos

                if self.body.pos.distance_to(prey.body.pos) < 5:
                    core.memory("agents").remove(prey)
                    self.body.hunger[0] -= 50
                    if self.body.hunger[0] < 0:
                        self.body.hunger[0] = 0
            else:
                self.body.acc = prey.pos - self.body.pos



    def show(self):
        self.body.show()

    def filtrePerception(self):
        pass


