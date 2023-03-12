from player import Player
import random
class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        # possible_actions = ["rock", "paper", "scissors", "spok", "lizard" ]
        self.choosen_gesture = random.choice(self.gestures)
        print(f"Ai chooses {self.choosen_gesture}")

    def round_score(self):
       return self.score > 2   
        
