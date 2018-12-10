import random

class Faller:
    def __init__(self):
        self.blocks = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
        self.pos = random.randint(0, 5)
        self.bottomBlock = 0
        self.bottomPos = -1
        self.moveRight = False
        self.moveLeft = False
        self.rollBlock = False
