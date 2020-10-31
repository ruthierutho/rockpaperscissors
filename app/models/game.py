from app.models.player import *

player1 = Player(Harry, rock)
player2 = Player(Ron, scissors)
player3 = Player(Hermione, paper)
players = [player1, player2, player3]

def play_game(player1, player2):
    if player1.move == rock and player2.move == paper:
        return f"{player2.name} wins by playing paper"
    if player1.move == rock and player2.move == scissors:
        return f"{player1.name} wins by playing rock"
    if player1.move == paper and player2.move == scissors
        return f"{player2.name} wins by playing scissors"
