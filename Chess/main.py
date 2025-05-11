from tkinter import mainloop
from classes.Figures import *
from classes.GameEngine import GameEngine
from proto_visualizator import *

##########################################

def coordinate_translater(loc) -> list:
    letter_to_number = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    y = 8 - int(loc[0])
    x = letter_to_number[loc[1]]
    return [x, y]

##########################################
# Основні взаємодії з грою
game = GameEngine()
game.deploy(Knight, "white", (2, 3))
game.deploy(Bishop, "black", (2, 2))
game.move((2, 2), (7, 7))

##########################################

draw_chessboard()

def update_board_visuals():
    circle_drawer.clear()
    for i, line in enumerate(game.board.space):
        for j, cell in enumerate(line):
            if cell:
                fig_color = "black" if cell.color == "black" else "white"
                fig_name = type(cell).__name__[:3]
                draw_circle_in_cell(j, i, color=fig_color, label=fig_name)


update_board_visuals()

def ask_for_move():
    try:
        move_input = input("Введіть хід (x1 y1 x2 y2): ")
        move = []
        move = [coordinate_translater(i) for i in move_input.strip().split()]
        move = move[0] + move[1]
        print(move)
        game.move((move[1], move[0]), (move[3], move[2]))
        update_board_visuals()
    except:
        print("Помилка вводу. Спробуйте ще раз.")
    # Запускаємо знову після 100 мс, щоб не блокувати GUI
    root.after(100, ask_for_move)

# Запускаємо цикл читання вводу
root.after(100, ask_for_move)

mainloop()
