import time

import core
from pygame import Vector2
from fustrum import Fustrum
from random import randint

class Body:
    def __init__(self):
        self.currTime = time.time()

        self.pos = Vector2(randint(10, core.WINDOW_SIZE[0] - 10), randint(10, core.WINDOW_SIZE[1] - 10))
        self.acc = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.fustrum = Fustrum()
        self.fustrum.body = self

        self.maxSpeed = 8
        self.maxAcc = 8
        self.hunger = [50, 55]
        self.tireness = [50, 51]
        self.reprod = [50, 52]
        self.birthdate = time.time(),

        self.lifespan = 500000000000.0

        self.dead = False
        self.sleep = False

        self.sleepTime = 0


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

        if self.sleepTime >= 50:
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
        return time.time() - self.birthdate[0] >= self.lifespan or self.hunger_dead()

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
        core.Draw.circle(self.color, self.pos, self.fustrum.ray, 1)

        if self.dead:
            core.Draw.circle((255, 255, 255), self.pos, 5)
        elif self.sleep:
            core.Draw.circle((0, 0 ,0), self.pos, 5)

    def is_reproductible(self):
        return self.reprod[0] >= self.reprod[1]