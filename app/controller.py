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


@app.route('/rock/paper')
def rock_paper():
    return "Paper beats rock!"

@app.route('/scissors/rock')
def scissors_rock():
    return "Rock beats scissors!"

@app.route('/scissors/paper')
def scissors_paper():
    return "Scissors beats paper!"

@app.route('/playgame')
def playing():
    return render_template('index.html', players=players)

@app.route('/gameplay')
def gameplay():
    playing_game = play_game(player1, player2)
    return render_template('index.html', players=players, winner=playing_game)

# @app.route('/choose-move', methods=['POST'])
# def choose_move():
#     new_name1 = request.form['name1']
#     new_move1 = request.form ['move1']
#     new_name2 = request.form['name2']
#     new_move2 = request.form ['move2']
#     new_player1 = Player(name=new_name1, move=new_move1)
#     new_player2 = Player(name=new_name2, move=new_move2)
#     add_new_player(new_player1)
#     add_new_player(new_player2)
#     playing_game = play_game(new_player1, new_player2)
#     return render_template('index.html', players=players, winner=playing_game)

@app.route('/choose-move', methods=['POST'])
def choose_move():
    new_name1 = request.form['name1']
    new_move1 = request.form ['move1']
    new_name2 = request.form['name2']
    new_move2 = request.form ['move2']
    new_player1 = Player(name=new_name1, move=new_move1)
    new_player2 = Player(name=new_name2, move=new_move2)
    new_players = [new_player1, new_player2]
   
    playing_game = play_game(new_player1, new_player2)
    return render_template('index.html', new_players=new_players, winner=playing_game)



