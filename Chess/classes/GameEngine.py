from classes.Board import Board
from classes.Figures import *

from Chess.classes.Figures import *


class GameEngine:
    def __init__(self):
        self.board = Board()

    def deploy(self, figure_class, color, location):
        self.board.space[location[0]][location[1]] = figure_class(color)

    def delite(self, location):
        self.board.space[location[0]][location[1]] = 0

    def move(self, from_location, to_location):
        # print(self.board.space[from_location[0]][to_location[1]])
        if self.board.space[from_location[0]][from_location[1]] and from_location != to_location:
            if self.board.space[from_location[0]][from_location[1]].get_possible_moves(pos= from_location, a= self.board.space, to_pos= to_location):
                print("Хід законний")
                self.board.space[to_location[0]][to_location[1]] = self.board.space[from_location[0]][from_location[1]]
                self.delite(from_location)
            else:
                raise Exception

    def reset(self):
        self.board = Board()
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece in enumerate(back_row):
            self.deploy(piece, "black", (0, col))
            self.deploy(Pawn, "black", (1, col))
            self.deploy(piece, "white", (7, col))
            self.deploy(Pawn, "white", (6, col))



