from app.models.player import *

player1 = Player("Harry", "paper")
player2 = Player("Ron", "rock")
# player3 = Player("Hermione", "scissors")
players = [player1, player2]


def add_new_player(player):
    players.append(player)

def play_game(player1, player2):
    if player1.move == "rock" and player2.move == "paper":
        return f"{player2.name} wins by playing paper"
    if player1.move == "paper" and player2.move == "rock":
        return f"{player1.name} wins by playing paper"
    if player1.move == "rock" and player2.move == "scissors":
        return f"{player1.name} wins by playing rock"
    if player1.move == "scissors" and player2.move == "rock":
        return f"{player2.name} wins by playing rock"
    if player1.move == "paper" and player2.move == "scissors":
        return f"{player2.name} wins by playing scissors"
    if player1.move == "scissors" and player2.move == "paper":
        return f"{player1.name} wins by playing scissors"
    if player1.move == player2.move:
        return "It's a draw!"

# def play_game_url(move1, move2):

