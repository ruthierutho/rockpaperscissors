from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *

# A route in a controller that takes in two wildcards e.g. (/<hand1>/<hand2>)
# A player class that takes in a name and the hand that was played, 
# e.g. Player("player 1", hand1)
# # A function to check which player won based on what was picked 
# in the url path(passed into the route in the controller), 
# (it will return: paper beats rock, scissors draws with scissors.) 
# e.g. check_win(player1, player2)

@app.route('/')
def greet():
    return "Hello"

@app.route('/<move1>/<move2>')
def playing(move1, move2):
    return play_game(player2, player3)




