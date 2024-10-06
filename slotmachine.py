from reels import *

class SlotMachine:
    def __init__(self):
        self.reels = [Reels(), Reels(), Reels(), Reels(), Reels()]

    def play(self, bet):
        output = [reel.spin() for reel in self.reels]
        print(output)

SlotMachine().play(1)
        