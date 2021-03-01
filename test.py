from unittest import TestCase
from app import app, boggle_game
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code , 200)

    def test_start_boggle(self):
        with app.test_client() as client:
            res = client.get('/start-boggle')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('table', html)
            self.assertEqual(session["num_of_plays"], 1)
            self.assertEqual(len(session["board"]), 5)
    
    # def test_check_word(self):
    #     with app.test_client() as client:
    #         res = client.get('/check-word')

    def test_submit_high_score(self):
        with app.test_client() as client:
            boggle_game.score = 10
            res = client.get('/submit-high-score')
            json = res.get_data(as_text=True)
            self.assertIn('10', json)

    def test_make_board(self):
        boggle_game = Boggle()
        board = boggle_game.make_board()
        self.assertEqual( 5 , len(board) )
        
    def test_check_valid_word(self):
        board = boggle_game.make_board()
        self.assertEqual('Not a Word!!!', boggle_game.check_valid_word(board, 'bLAHbBls'))
