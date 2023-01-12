from agent import Agent
from carnivoreagent import CarnivoreAgent
from superpredatorbody import SuperpredatorBody


class SuperpredatorAgent(Agent):
    def __init__(self):
        super().__init__(SuperpredatorBody())


    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.body.pos)
            if isinstance(p, CarnivoreAgent):
                prey.append(p)

        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger