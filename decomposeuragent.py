from agent import Agent
from decomposeurbody import DecomposeurBody
from vegetal import Vegetal


class DecomposeurAgent(Agent):
    def __init__(self):
        super().__init__(DecomposeurBody())


    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.body.pos)
            if (isinstance(p, Agent) and not isinstance(p, DecomposeurAgent) and p.body.dead)\
                    or isinstance(p, Vegetal):
                prey.append(p)

        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger

