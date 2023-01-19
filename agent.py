from random import randint
from random import uniform
from corner import Corner
from pygame import Vector2

import core


class Agent:
    def __init__(self, body):
        self.id = randint(1, 100000000)
        self.body = body
        self.perception = []
        self.hunting = False

    def update(self):
        self.hunting = self.body.hunger[0] / self.body.hunger[1] > 0.5 and not self.body.dead
        preys, dangers, symbs = self.filtrePerception()
        if len(dangers) > 0 and len(symbs) > 0:
            self.run_to(symbs[0].pos)

        elif len(dangers) > 0 and len(symbs) == 0:
            self.run_from(dangers)

        elif len(preys) > 0 and len(symbs) > 0 and len(dangers) == 0:
            if self.hunting:
                self.run_to(preys[0].pos)
                self.eat(preys[0])
            else:
                self.run_to(symbs[0].pos)

        elif len(preys) > 0 and self.hunting:
            prey = preys[0]
            self.body.acc = prey.pos - self.body.pos
            self.eat(prey)

        else:
            self.body.acc = Vector2(uniform(-1, 1), uniform(-1, 1))




    def run_to(self, pos):
        self.body.acc = pos - self.body.pos

    def run_from(self, predators):
        self.body.acc = self.body.acc - self.fear(predators)

    def fear(self, predators):
        steering = Vector2()
        predatorCounter = 0
        for predator in predators:
            if self.body.pos.distance_to(predator.pos) != 0:
                diff = Vector2(predator.pos.x - self.body.pos.x, predator.pos.y - self.body.pos.y)
                if diff.length() > 0.001:
                    diff.scale_to_length(self.body.pos.distance_squared_to(predator.pos))
                    predatorCounter += 1
                    steering += diff
            else:
                steering += Vector2(uniform(-5, 5), uniform(-5, 5))
                predatorCounter += 1

        if predatorCounter > 0:
            steering /= predatorCounter

            steering += self.body.speed

            if steering.length() > self.body.maxAcc:
                steering = steering.normalize()
                steering.scale_to_length(self.body.maxAcc)
        return steering

    def eat(self, prey):
        if self.body.pos.distance_to(prey.pos) < 5:
            prey.is_eaten = True
            self.update_hunger()

    def update_hunger(self):
        self.body.hunger[0] -= 5
        if self.body.hunger[0] < 0:
            self.body.hunger[0] = 0

    def show(self):
        self.body.show()
        if self.hunting:
            core.Draw.circle(self.body.color, self.body.pos, 15, 1)

    def filtrePerception(self):
        pass

    def append_corner_as_danger(self, item, dangers):
        if isinstance(item, Corner) and len(dangers) > 0:
            dangers.append(item)


