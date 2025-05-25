import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
from classes.Figures import *
from classes.GameEngine import GameEngine
import os

CELL_SIZE = 60  # ← відповідає розміру зображення
BOARD_SIZE = 8

LIGHTCOLOR = "#EEEED2"
DARKCOLOR = "#769656"

IMAGE_DIR = "classes/images"

root = tk.Tk()
root.title("Шахи")

frame = tk.Frame(root)

controls = tk.Frame(root)
controls.pack()

def on_reset():
    global is_rotated
    is_rotated = False
    game.reset()
    draw_board()

def on_rotate():
    global is_rotated
    is_rotated = not is_rotated
    draw_board()

tk.Button(controls, text="Reset", command=on_reset).pack(side=tk.LEFT, padx=5)
tk.Button(controls, text="Rotate", command=on_rotate).pack(side=tk.LEFT, padx=5)


frame.pack()

buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
images_cache = {}

game = GameEngine()
is_rotated = False

# Розміщуємо фігури
game.reset()
# game.deploy(Knight, "white", (2, 3))
# game.deploy(Bishop, "black", (2, 2))
# game.deploy(Rook, "white", (1, 1))


class Observer:
    def __init__(self):
        self.selected = []

    def on_cell_click(self, x, y):
        print(f"Клік: ({x}, {y})")
        self.selected.append((y, x))

        if len(self.selected) == 2:
            src, dst = self.selected
            print(f"Спроба перемістити з {src} до {dst}")
            try:
                game.move(src, dst)
                print("Хід успішний")
            except Exception as e:
                print("Помилка при ході:", e)
            self.selected = []
            draw_board()


observer = Observer()


def load_image(icon_name):
    if icon_name in images_cache:
        return images_cache[icon_name]

    path = os.path.join(IMAGE_DIR, icon_name)
    try:
        img = Image.open(path)
        img = img.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        images_cache[icon_name] = img_tk
        return img_tk
    except FileNotFoundError:
        print(f"❌ Не знайдено зображення: {path}")
        return None


def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Обчислення координат з урахуванням повороту
            x, y = (col, row)
            if is_rotated:
                x, y = row, BOARD_SIZE - col - 1

            cell = game.board.space[y][x]
            bg = LIGHTCOLOR if (x + y) % 2 == 0 else DARKCOLOR

            icon_name = cell.icon if cell and hasattr(cell, "icon") else "empty.png"
            icon_img = load_image(icon_name)

            if buttons[row][col] is None:
                button = tk.Button(
                    frame,
                    width=CELL_SIZE,
                    height=CELL_SIZE,
                    bg=bg,
                    command=partial(observer.on_cell_click, x, y),
                    borderwidth=0,
                    highlightthickness=0
                )
                button.grid(row=row, column=col, padx=0, pady=0)
                buttons[row][col] = button

            btn = buttons[row][col]
            btn.config(image=icon_img, bg=bg)
            btn.image = icon_img


draw_board()
root.mainloop()
