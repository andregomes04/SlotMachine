from reels import *
import numpy as np

class SlotMachine:
    def __init__(self):
        self.reels = [Reels(), Reels(), Reels(), Reels(), Reels()]
        self.paytable = {
            (0, 0, 0): 0.5, (0, 0, 0, 0): 1.2, (0, 0, 0, 0, 0): 12.0,
            (1, 1, 1): 0.8, (1, 1, 1, 1): 2.0, (1, 1, 1, 1, 1): 25.0,
            (2, 2, 2): 1.5, (2, 2, 2, 2): 3.0, (2, 2, 2, 2, 2): 50.0,
            (3, 3, 3): 2.5, (3, 3, 3, 3): 5.0, (3, 3, 3, 3, 3): 100.0
        }

    def contains_pay(self, lst, sublst):
        n = len(lst)
        m = len(sublst)

        for i in range(n - m + 1):
            if lst[i:i + m] == sublst:
                return True
        return False
    
    def check_paytable(self, matrix, paytable):
        total_multiplier = 0
        for row in matrix:
            for key in paytable.keys():
                if self.contains_pay(row, list(key)):
                    total_multiplier = self.paytable[key]

        return total_multiplier

    def play(self, bet):
        output = [reel.spin() for reel in self.reels]
        matrix = [list(row) for row in zip(*output)]
        print(matrix)

        payout = bet * self.check_paytable(matrix, self.paytable)
        print("You won: ", payout) if payout > 0 else print("You lost!")
        return payout
    
    # def calculate_rtp(self, plays, bet_amount):
    #    total_bet = plays * bet_amount
    #    total_payout = 0

    #    for _ in range(plays):
    #       total_payout += self.play(bet_amount)

    #    rtp = (total_payout / total_bet) * 100
    #    print(rtp)

    #SlotMachine().calculate_rtp(1000000, 10)
                   

SlotMachine().play(0.10)
        