from agent import Agent
from herbivorebody import HerbivoreBody
from vegetal import Vegetal

class HerbivoreAgent(Agent):
    def __init__(self):
        super().__init__(HerbivoreBody())

    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.body.pos)
            if isinstance(p, Vegetal):
                prey.append(p)
            elif p.__class__.__name__ == "CarnivoreAgent":
                danger.append(p)
        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger