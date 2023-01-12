from random import uniform
from vivarium import vivarium
from body import Body

class DecomposeurBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (117, 86, 0)

        self.maxAcc = uniform(vivarium["decomposeur"]["params"]["maxAcc"]["min"],
                              vivarium["decomposeur"]["params"]["maxAcc"]["max"])
        self.maxSpeed = uniform(vivarium["decomposeur"]["params"]["maxSpeed"]["min"],
                              vivarium["decomposeur"]["params"]["maxSpeed"]["max"])


        self.tireness = [0, uniform(vivarium["decomposeur"]["params"]["tireness"]["min"],
                              vivarium["decomposeur"]["params"]["tireness"]["max"])]
        self.hunger = [0, uniform(vivarium["decomposeur"]["params"]["hunger"]["min"],
                              vivarium["decomposeur"]["params"]["hunger"]["max"])]
        self.reprod = [0, uniform(vivarium["decomposeur"]["params"]["reprod"]["min"],
                              vivarium["decomposeur"]["params"]["reprod"]["max"])]