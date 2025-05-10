from classes.Figures import *
from classes.GameEngine import GameEngine

game = GameEngine()
game.deploy(Bishop, "black", (2, 2))
for line in game.board.space:
    print(line)
print(" ")
print(" ")
game.move((2,2),(7,7))
for line in game.board.space:
    print(line)
