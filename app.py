from flask import Flask, render_template, session, jsonify, request
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pqio'
boggle_game = Boggle()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start-boggle')
def start_boggle():
    """Reset game score, save board to session , and render game board."""
    if not session.get("num_of_plays", 0):
        session["num_of_plays"] = 1
    else: 
        session["num_of_plays"] += 1
    print(session["num_of_plays"])
    boggle_game.score = 0
    
    board_size = request.args.get("custom-size", request.args["board-size"])

    board = boggle_game.make_board(int(board_size))
    session["board"] = board

    return render_template('start-boggle.html', words_list=board)

@app.route('/check-word')
def check_word():
    """Recieve guess from form. Send JSON object containing result, score, and the guess"""
    guess = request.args["guess"]
    result = boggle_game.check_valid_word(session["board"], guess)

    return jsonify(result=result, score=boggle_game.score, guess=guess)

@app.route('/submit-high-score')
def submit_high_score():
    """Set a high score in session if there wasn't one already.
    Update high score if current game's score is higher than saved high score.
    """
    current_score = boggle_game.score

    if not session.get("high_score", False):
        session["high_score"] = current_score
    else:    
        if current_score > session["high_score"]:
            session["high_score"] = current_score

    return jsonify(highscore=session["high_score"])

