from body import Body


class SuperpredatorBody(Body):
    def __init__(self, body):
        super().__init__(body)
        self.color = (0,0,255)