from classes.Board import Board
from classes.Figures import *
from Chess.classes.Figures import *


class GameEngine:
    def __init__(self):
        self.board = Board()
        self.turn = "white"  # білий починає
        self.last_move = None
        self.status = "continue"

    def deploy(self, figure_class, color, location):
        self.board.space[location[0]][location[1]] = figure_class(color)

    def delite(self, location):
        self.board.space[location[0]][location[1]] = None

    def move(self, from_location, to_location):
        # print(self.board.space[from_location[0]][to_location[1]])
        piece = self.board.space[from_location[0]][from_location[1]]
        if piece and from_location != to_location and piece.color == self.turn and self.status == "continue":
            if piece.get_possible_moves(pos= from_location, a= self.board.space, to_pos= to_location):

                print("Хід законний")

                self.board.space[to_location[0]][to_location[1]] = self.board.space[from_location[0]][from_location[1]]
                self.delite(from_location)

                self.last_move = (from_location, to_location)
                self.turn = "black" if self.turn == "white" else "white"

                if self.is_check(color=self.turn):
                    print("Шах")
                    if self.is_checkmate(self.turn):
                        self.status = "finish"
                        print("Мат")
                else:
                    print("Все ок")



            else:
                print("Хід незаконний")
                raise Exception


    def reset(self):
        self.board = Board()
        self.turn = "white"
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece in enumerate(back_row):
            self.deploy(piece, "black", (0, col))
            self.deploy(Pawn, "black", (1, col))
            self.deploy(piece, "white", (7, col))
            self.deploy(Pawn, "white", (6, col))

    def is_check(self, color)->bool:
        king_pos = None
        for r in range(8):
            for c in range(8):
                piece = self.board.space[r][c]
                if piece and piece.name == "king" and piece.color == color:
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        for r in range(8):
            for c in range(8):
                piece = self.board.space[r][c]
                if piece and piece.color != color:
                    if piece.get_possible_moves((r, c), self.board.space, king_pos, self.last_move):
                        return True
        return False

    def is_checkmate(self, color)->bool:
        if not self.is_check(color):
            return False

        for r1 in range(8):
            for c1 in range(8):
                piece = self.board.space[r1][c1]
                if piece and piece.color == color:
                    for r2 in range(8):
                        for c2 in range(8):
                            backup = self.board.space[r2][c2]
                            from_pos = (r1, c1)
                            to_pos = (r2, c2)
                            if piece.get_possible_moves(from_pos, self.board.space, to_pos, self.last_move):
                                self.board.space[r2][c2] = piece
                                self.board.space[r1][c1] = None
                                in_check = self.is_check(color)
                                self.board.space[r1][c1] = piece
                                self.board.space[r2][c2] = backup
                                if not in_check:
                                    return False
        return True

################



