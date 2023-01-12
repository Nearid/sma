class Fustrum:
    def __init__(self):
        self.body = None
        self.ray = 100


    def inside(self, pos, weight=0):
        return self.body.pos.distance_to(pos) < self.ray + weight