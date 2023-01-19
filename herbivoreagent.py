from agent import Agent
from herbivorebody import HerbivoreBody
from vegetal import Vegetal


class HerbivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(HerbivoreBody(body))

    def filtrePerception(self):
        prey = []
        danger = []
        symb = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.pos)
            if isinstance(p, Vegetal):
                prey.append(p)
            elif p.__class__.__name__ == "CarnivoreBody" and not p.dead:
                danger.append(p)
            elif p.__class__.__name__ == "SuperpredatorBody" and not p.dead:
                symb.append(p)
            else:
                super().append_corner_as_danger(p, danger)
        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        symb.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger, symb
