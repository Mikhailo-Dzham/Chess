class GameEngine:
    def __init__(self):
        self.board = Board()

class Judge:
    pass

class Board:
    def __init__(self):
        self.space = [[0 for _ in range(8)] for _ in range(8)]

class Figure:
    pass

class Pawn(Figure):
    pass

class Knight(Figure):
    pass

class King(Figure):
    pass

class Queen(Figure):
    pass

class Bishop(Figure):
    pass

class Rook(Figure):
    pass