from classes.Figure import Figure
from classes.Figures import *


class Board:
    def __init__(self):
        self.space = [[0 for _ in range(8)] for _ in range(8)]


    def deploy_rook(self, name, color, location):
        self.space[location[0]][location[1]] = Rook(color)