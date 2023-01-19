from agent import Agent
from carnivorebody import CarnivoreBody
from herbivorebody import HerbivoreBody

class CarnivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(CarnivoreBody(body))

    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.pos)
            if isinstance(p, HerbivoreBody):
                prey.append(p)
            elif p.__class__.__name__ == "SuperpredatorBody" and not p.dead:
                danger.append(p)
            else:
                super().append_corner_as_danger(p, danger)

        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger, []