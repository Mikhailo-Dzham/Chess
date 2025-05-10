from classes.Board import Board
from classes.Figures import *

class GameEngine:
    def __init__(self):
        self.board = Board()

    def deploy(self, figure_class, color, location):
        self.board.space[location[0]][location[1]] = figure_class(color)

    def delite(self, location):
        self.board.space[location[0]][location[1]] = 0

    def move(self, from_location, to_location):
        self.board.space[to_location[0]][to_location[1]] = self.board.space[from_location[0]][from_location[1]]
        self.delite(from_location)