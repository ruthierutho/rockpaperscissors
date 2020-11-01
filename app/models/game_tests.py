import unittest

from app.models.game import *
from app.models.player import Player

class TestGame(unittest.TestCase):
    


    def test_play_game(self):
        play_game(player1, player3)
        self.assertEqual("Harry wins by playing rock", play_game(player1, player3))

    def test_play_game_draw(self):
        player2= Player("Ron", "paper")
        player3= Player("Hermione", "paper")
        play_game(player2, player3)
        self.assertEqual("It's a draw!", play_game(player2, player3))
