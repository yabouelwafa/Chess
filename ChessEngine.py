"""
Storing Data and determining the valid moves and keeping a move log.
"""

class GameState:
    def __init__(self):
        #Board is 8x8 2-dimensional list
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        if move.pieceCaptured[0] != move.pieceMoved[0] and move.pieceMoved != '--':
            if self.whiteToMove and move.pieceMoved[0] == 'w' or not self.whiteToMove and move.pieceMoved[0] == 'b':
                self.board[move.startRow][move.startCol] = "--"
                self.board[move.endRow][move.endCol] = move.pieceMoved
                self.moveLog.append(move)
                self.whiteToMove = not self.whiteToMove
                return True
        return False

class Move:

    ranksToRows = {"1" : 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]

        self.endRow = endSq[0]
        self.endCol = endSq[1]

        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, c, r):
        return self.colsToFiles[c] + self.rowsToRanks[r]

