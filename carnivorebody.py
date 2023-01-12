import core
from random import uniform
from vivarium import vivarium
from body import Body

class CarnivoreBody(Body):
    def __init__(self):
        super().__init__()
        self.maxAcc = 10
        self.maxSpeed = 10
        self.color = (255, 0, 0)

        self.maxAcc = uniform(vivarium["carnivore"]["params"]["maxAcc"]["min"],
                              vivarium["carnivore"]["params"]["maxAcc"]["max"])
        self.maxSpeed = uniform(vivarium["carnivore"]["params"]["maxSpeed"]["min"],
                              vivarium["carnivore"]["params"]["maxSpeed"]["max"])
        self.tireness = [0, uniform(vivarium["carnivore"]["params"]["tireness"]["min"],
                              vivarium["carnivore"]["params"]["tireness"]["max"])]

        self.hunger = [0, uniform(vivarium["carnivore"]["params"]["hunger"]["min"],
                              vivarium["carnivore"]["params"]["hunger"]["max"])]
        self.reprod = [0, uniform(vivarium["carnivore"]["params"]["reprod"]["min"],
                              vivarium["carnivore"]["params"]["reprod"]["max"])]