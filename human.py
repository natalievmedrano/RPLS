from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        for i in range(len(self.gestures)):
            print(f'{i + 1}) {self.gestures[i]}')

        index = int(input("Please choose a gesture: "))

        self.selected_gesture = self.gestures[index - 1]

        print(f"Human player chooses {self.selected_gesture}")    

    def round_score(self):
       return self.score > 2