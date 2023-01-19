from agent import Agent
from carnivorebody import CarnivoreBody
from superpredatorbody import SuperpredatorBody


class SuperpredatorAgent(Agent):
    def __init__(self, body):
        super().__init__(SuperpredatorBody(body))


    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            p.dist = self.body.pos.distance_to(p.pos)
            if isinstance(p, CarnivoreBody):
                prey.append(p)
            else:
                super().append_corner_as_danger(p, danger)

        prey.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return prey, danger, []