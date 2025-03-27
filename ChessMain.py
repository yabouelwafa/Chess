"""
Displaying Data
"""

import pygame as p
from pygame.examples.sprite_texture import running

import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #Chess boards are 8 x 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #For animation
IMAGES = {}

'''
Initialize a global dictionary of images. Called exactly once in its main.
'''
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #We can access each image in the dictionary now because they are all loaded

'''
Main driver to handle user input and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    load_images()
    running = True

    sqSelected = ()
    playerClicks = []

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #x, y location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2: #after 2nd click
                    move =  ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    validMove = gs.makeMove(move)
                    if validMove:
                        print(move.getChessNotation())


                    sqSelected = ()
                    playerClicks = []

            square = sqSelected
            drawGameState(screen, gs, square)
            clock.tick(MAX_FPS)
            p.display.flip()


'''
Responsible for graphics
'''
def drawGameState(screen, gs, square):
    drawBoard(screen) #draw the squares on the board

    highlightSq(screen, square)
    drawPieces(screen, gs.board)

'''Draw the squares'''
def drawBoard(screen):
    colors = [p.Color("beige"), p.Color("tan")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(c + r) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''Draw the pieces'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], (c * SQ_SIZE, r * SQ_SIZE))

'''Highlight the selected piece'''
def highlightSq(screen, square):
    if square != ():
        s = p.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('yellow'))
        screen.blit(s, (square[1] * SQ_SIZE, square[0] * SQ_SIZE))

if __name__ == '__main__':
    main()