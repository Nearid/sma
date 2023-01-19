from body import Body


class HerbivoreBody(Body):
    def __init__(self, body):
        super().__init__(body)
        self.color = (0, 255, 0)