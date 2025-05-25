from classes.Figure import Figure

class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}R.png"

    def get_possible_moves(self, pos, a, to_pos,  last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if not a[nr][nc]:
                    m.append((nr, nc))
                elif a[nr][nc].color != self.color:
                    m.append((nr, nc))
                    break
                else:
                    break
                nr += dr
                nc += dc
        avl = False
        if to_pos in m:
            avl = True
        return avl
        
class Bishop(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}B.png"

class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}K.png"

class Queen(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}Q.png"

class Knight(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}N.png"

class Pawn(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}p.png"

