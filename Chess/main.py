
from classes.GameEngine import GameEngine

game = GameEngine()
game.board.deploy_rook("df", "black", (2, 2))
for line in game.board.space:
    print(line)
