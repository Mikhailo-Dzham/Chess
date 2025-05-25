from classes.Figure import Figure
from classes.Figures import *


class Board:
    def __init__(self):
        self.space = [[None for _ in range(8)] for _ in range(8)]