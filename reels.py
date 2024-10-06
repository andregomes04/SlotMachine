import random

class Reels:
    def __init__(self):
        self.reel = [0, 1, 2, 3]

    def spin(self):
        symbols = []
        for i in range(3):
            symbol = (random.choices(self.reel, weights=[0.4, 0.3, 0.2, 0.1], k=1))[0]
            symbols.append(symbol)
        return symbols
    