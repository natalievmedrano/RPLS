class Player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock" ]
        self.score = 0
        self.selected_gesture = ""

    def score_point(self):
         self.score += 1
    
    def choose_gesture(self):
     pass

    def winning_choice(self):
        self.score = 2
    