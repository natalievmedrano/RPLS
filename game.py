from human import Human
from player import Player
from ai import Ai

# Welcome to Rock Paper Scissors Lizard Spock.

# each match will be best of three games

# Scissors cuts paper 
# paper covers rock 
# rock crushes lizard 
# lizard poisons Spock 
# Spock smashes scissors 
# scissors decapitates lizard 
# lizard eats paper 
# paper disproves Spock 
# Spock vaporizes rock 
# Rock crushes scissors.

# Use the number keys to enter your selection

class Game:    
    def __init__(self):
        self.player1 = Human()
        self.player2 = Ai()

    def display_greeting(self):
    
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print("Each match will be best of three games!")

        

    def display_rules(self):
        print (f'''
Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
''')
    def select_player_type(self):
        response = input("How many players will play in this game? (1, 2) Use the number keys to enter your selection ")
        if response == "2":
            self.player2 = Human()         
            # print("Use the number keys to enter your selection")
        # response = "1"
        # # if response  "1":
            

        # if response == "1":
        #     print(input("What do you choose for your first gesture?"))
        
        # self.choose_gesture = ''
        # self.game_score = 0


    def compare_gestures(self):
        if self.player1.selected_gesture == self.player2.selected_gesture:
            print("It's a tie!")
        elif self.player1.selected_gesture == "Rock":
            if self.player2.selected_gesture == "Scissors" or self.player2.selected_gesture == "Lizard":
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.selected_gesture == "Scissors":
            if self.player2.selected_gesture == "Paper" or self.player2.selected_gesture == "Lizard":
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.selected_gesture == "Paper":
            if self.player2.selected_gesture == "Rock" or self.player2.selected_gesture == "Spock":
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.selected_gesture == "Lizard":
            if self.player2.selected_gesture == "Spock" or self.player2.selected_gesture == "Paper":
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.selected_gesture == "Spock":
            if self.player2.selected_gesture == "Scissors" or self.player2.selected_gesture == "Rock":
                self.player1.score_point()
            else:
                self.player2.score_point() 
                                                       
    
    def keep_score(self):
        print (f"Human Score {self.player1.score}")
        print (f"Ai Score {self.player2.score}")



    def game_winner(self):
        if self.player1.score >= 2:
            print("Human wins the game!")
        elif self.player2.score >= 2:
            print("Ai wins the game!")
    
    def choose_gestures(self):
        self.player1.choose_gesture()
        self.player2.choose_gesture()
    

    def run_round(self):
          while self.player1.score < 2 and self.player2.score < 2:
                self.keep_score()
                self.choose_gestures()  
                self.compare_gestures()
                self.keep_score()
                self.game_winner()
            #print()
            
            #print()
            #self.keep_score()
           # print()
           # print('NEXT ROUND')
            
        
    
    
    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.select_player_type()
        self.run_round()
    
        # self.game_winner()
        
