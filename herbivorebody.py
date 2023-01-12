from body import Body
from agent import Agent
from vegetal import Vegetal
from random import uniform
from vivarium import vivarium
class HerbivoreBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 0)
        self.maxAcc = uniform(vivarium["herbivore"]["params"]["maxAcc"]["min"],
                              vivarium["herbivore"]["params"]["maxAcc"]["max"])
        self.maxSpeed = uniform(vivarium["herbivore"]["params"]["maxSpeed"]["min"],
                              vivarium["herbivore"]["params"]["maxSpeed"]["max"])
        self.tireness = [0, uniform(vivarium["herbivore"]["params"]["tireness"]["min"],
                              vivarium["herbivore"]["params"]["tireness"]["max"])]
        self.hunger = [0, uniform(vivarium["herbivore"]["params"]["hunger"]["min"],
                              vivarium["herbivore"]["params"]["hunger"]["max"])]
        self.reprod = [0, uniform(vivarium["herbivore"]["params"]["reprod"]["min"],
                              vivarium["herbivore"]["params"]["reprod"]["max"])]


    def filtrePerception(self):
        prey = []
        danger = []
        for p in self.perception:
            if isinstance(p, Agent) and p.dead:
                prey.append(p)
            elif isinstance(p, Vegetal):
                danger.append(p)
        return prey, danger