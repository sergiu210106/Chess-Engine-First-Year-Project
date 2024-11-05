'''
This is our main driver file. It is responsible for handling user input and displaying the current game_state object.
'''

import pygame as p
from chess import chess_engine

p.init()
WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 # chess boards are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}


'''
Initialize a global dictionary of images. This will be called exactly once in the main.
'''

def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Note: we can access an image by saying 'IMAGES["wp"]'

'''
The main driver for our code. This will handle user input and updating the graphics.
'''

def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = chess_engine.game_state()
    load_images() # only once, before the loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False


        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Responsible for all the graphics within a current game state.
'''
def draw_game_state(screen, gs):
    draw_board(screen) # draw squares on the board
    # add in piece highlighting or move suggestions
    draw_pieces(screen, gs.board) # draw pieces on top of the squares

'''
Draw the squares on the board
'''
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current game_state.board
'''
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # not an empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
if __name__ == '__main__':
    main()