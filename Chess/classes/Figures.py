from classes.Figure import Figure

class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}R.png"
        self.name = "rook"

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
        self.name = "bishop"
        super().__init__(color)
        self.icon = f"{color[0]}B.png"

    def get_possible_moves(self, pos, a, to_pos, last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
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
        return to_pos in m

class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}K.png"
        self.name = "king"

    def get_possible_moves(self, pos, a, to_pos, last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                if not a[nr][nc] or a[nr][nc].color != self.color:
                    m.append((nr, nc))
        return to_pos in m

class Queen(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}Q.png"
        self.name = "queen"

    def get_possible_moves(self, pos, a, to_pos, last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]:
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
        return to_pos in m

class Knight(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}N.png"
        self.name = "knight"

    def get_possible_moves(self, pos, a, to_pos, last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                if not a[nr][nc] or a[nr][nc].color != self.color:
                    m.append((nr, nc))
        return to_pos in m

class Pawn(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.icon = f"{color[0]}p.png"
        self.name = "pawn"

    def get_possible_moves(self, pos, a, to_pos, last_move=None) -> bool:
        m, r, c = [], pos[0], pos[1]
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        # 1 крок вперед
        if 0 <= r + direction < 8 and not a[r + direction][c]:
            m.append((r + direction, c))
            # 2 кроки вперед з початкової позиції
            if r == start_row and not a[r + 2 * direction][c]:
                m.append((r + 2 * direction, c))

        # б'єм по діагоналі
        for dc in [-1, 1]:
            nc = c + dc
            nr = r + direction
            if 0 <= nc < 8 and 0 <= nr < 8:
                target = a[nr][nc]
                if target and target.color != self.color:
                    m.append((nr, nc))

        # en passant
        # if last_move and isinstance(last_move["piece"], Pawn):
        #     last_from_r, last_from_c = last_move["from"]
        #     last_to_r, last_to_c = last_move["to"]
        #     if abs(last_to_r - last_from_r) == 2:  # пішак зробив 2 кроки
        #         if last_to_r == r and abs(last_to_c - c) == 1:
        #             m.append((r + direction, last_to_c))

        return to_pos in m

