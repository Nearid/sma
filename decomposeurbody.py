from body import Body

class DecomposeurBody(Body):
    def __init__(self, body):
        super().__init__(body)
        self.color = (117, 86, 0)