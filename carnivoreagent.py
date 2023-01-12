from agent import Agent
from carnivorebody import CarnivoreBody
from herbivoreagent import HerbivoreAgent

class CarnivoreAgent(Agent):
    def __init__(self):
        super().__init__(CarnivoreBody())


    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.body.pos)
            if isinstance(p, HerbivoreAgent):
                prey.append(p)
            elif p.__class__.__name__ == "SuperpredatorAgent":
                danger.append(p)

        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger