import time

import core
from pygame import Vector2
from fustrum import Fustrum
from random import randint, uniform

EVOLUTION_RATE = 0.1


def evolve(value, evoRate=EVOLUTION_RATE):
    rate = value * evoRate
    randomValue = uniform(value - rate, value + rate)
    if randomValue <= 0:
        randomValue = 0.1
    return randomValue


class Body:
    def __init__(self, body):
        self.init()
        if body is None:
            self.pos = Vector2(randint(10, core.WINDOW_SIZE[0] - 10), randint(10, core.WINDOW_SIZE[1] - 10))
            self.maxSpeed = 0
            self.maxAcc = 0
            self.hunger = [0, 0]
            self.tireness = [0, 0]
            self.reprod = [0, 0]
        else:
            self.maxAcc = evolve(body.maxAcc)
            self.maxSpeed = evolve(body.maxSpeed)
            self.hunger = [0, evolve(body.hunger[1])]
            self.tireness = [0, evolve(body.tireness[1])]
            self.reprod = [0, evolve(body.reprod[1])]
            self.birthdate = time.time()
            self.lifespan = evolve(body.lifespan)
            self.pos = Vector2(evolve(body.pos.x, 0.01), evolve(body.pos.y, 0.01))

    def init(self):
        self.acc = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.currTime = time.time()
        self.birthdate = time.time()
        self.dead = False
        self.sleep = False
        self.is_eaten = False
        self.sleepTime = 0
        self.deadTime = 0
        self.fustrum = Fustrum()
        self.fustrum.body = self

    def move(self):
        if self.sleep or self.dead:
            self.speed = Vector2(0, 0)
            return

        if self.acc.length() > self.maxAcc:
            self.acc.scale_to_length(self.maxAcc)

        self.speed += self.acc

        if self.speed.length() > self.maxSpeed:
            self.speed.scale_to_length(self.maxSpeed)

        self.pos += self.speed
        self.acc = Vector2(0, 0)
        self.edge()

    def update(self):
        if self.sleep:
            self.sleepTime += 1

        if self.dead:
            self.deadTime += 1

        if self.sleepTime >= core.fps * 5:
            self.tireness[0] = 0
            self.sleepTime = 0
            self.sleep = False

        if self.has_passed_1_sec():
            self.tireness[0] += 1
            self.hunger[0] += 1
            self.reprod[0] += 1

        if self.tireness[0] >= self.tireness[1]:
            self.sleep = True

        if self.is_dead():
            self.sleep = False
            self.dead = True

    def is_dead(self):
        return time.time() - self.birthdate >= self.lifespan or self.hunger_dead()

    def hunger_dead(self):
        return self.hunger[0] >= self.hunger[1]

    def edge(self):
        if self.pos.x < 0:
            self.speed.x *= -1
            self.pos.x = 0
        elif self.pos.x > core.WINDOW_SIZE[0]:
            self.speed.x *= -1
            self.pos.x = core.WINDOW_SIZE[0]

        if self.pos.y < 0:
            self.speed.y *= -1
            self.pos.y = 0
        elif self.pos.y > core.WINDOW_SIZE[1]:
            self.speed.y *= -1
            self.pos.y = core.WINDOW_SIZE[1]

    def has_passed_1_sec(self):
        if time.time() - self.currTime >= 1:
            self.currTime = time.time()
            return True
        return False

    def show(self):
        core.Draw.circle(self.color, self.pos, 10)

        if self.dead:
            core.Draw.circle((255, 255, 255), self.pos, 5)
        elif self.sleep:
            core.Draw.circle((0, 0, 0), self.pos, 5)

    def is_reproductible(self):
        return self.reprod[0] >= self.reprod[1] and not self.dead
