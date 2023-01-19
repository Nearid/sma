from pygame import Vector2
from random import randint
import core
class Item:
    def __init__(self):
        self.pos = Vector2(randint(10, core.WINDOW_SIZE[0] - 10), randint(10, core.WINDOW_SIZE[1] - 10))
        self.is_eaten = False

    def show(self):
        core.Draw.circle((50, 255, 0), self.pos, 3)