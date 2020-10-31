from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def greet():
    return "Hello"

@app.route('/<play>/<play2>')
def playing(play, play2):
    return game.playgame(player1, player2)



