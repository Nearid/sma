from body import Body
from random import uniform
from vivarium import  vivarium

class SuperpredatorBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (0,0,255)


        self.maxAcc = uniform(vivarium["superpredator"]["params"]["maxAcc"]["min"],
                              vivarium["superpredator"]["params"]["maxAcc"]["max"])
        self.maxSpeed = uniform(vivarium["superpredator"]["params"]["maxSpeed"]["min"],
                              vivarium["superpredator"]["params"]["maxSpeed"]["max"])
        self.tireness = [0, uniform(vivarium["superpredator"]["params"]["tireness"]["min"],
                              vivarium["superpredator"]["params"]["tireness"]["max"])]
        self.hunger = [0, uniform(vivarium["superpredator"]["params"]["hunger"]["min"],
                              vivarium["superpredator"]["params"]["hunger"]["max"])]
        self.reprod = [0, uniform(vivarium["superpredator"]["params"]["reprod"]["min"],
                              vivarium["superpredator"]["params"]["reprod"]["max"])]