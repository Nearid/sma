from body import Body


class CarnivoreBody(Body):
    def __init__(self, body):
        super().__init__(body)
        self.color = (255, 0, 0)