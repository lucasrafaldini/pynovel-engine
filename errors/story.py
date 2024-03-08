class StoryCohesionError(Exception):
    def __init__(self, message="Story cohesion error: The story is not cohesive."):
        self.message = message
        super().__init__(self.message)
