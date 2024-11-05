'''
This class is responsible for storing all the information about the current state of a chess game. It will also be responsible for
determining the valid moves at the current state. It will also keep a move log.
'''

class game_state():
    def __init__(self):
        # the board is an 8x8 2-dimensional list, each element has 2 characters.
        # the first - the color of the piece : 'b' or 'w'
        # the second - the type of the piece : 'K', 'Q', 'R', 'B', 'N' or 'P'
        # '--' represents an empty space or no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []