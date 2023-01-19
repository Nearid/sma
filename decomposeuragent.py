from body import Body
from agent import Agent
from decomposeurbody import DecomposeurBody
from vegetal import Vegetal


class DecomposeurAgent(Agent):
    def __init__(self, body):
        super().__init__(DecomposeurBody(body))

    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.pos)
            if (isinstance(p, Body) and not isinstance(p, DecomposeurBody) and p.dead)\
                    or isinstance(p, Vegetal):
                prey.append(p)
            else:
                super().append_corner_as_danger(p, danger)
        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger, []

