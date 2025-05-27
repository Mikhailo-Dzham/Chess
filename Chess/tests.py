import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
from classes.Figures import *
from classes.GameEngine import GameEngine
import os

#######################

#######################

CELL_SIZE = 60  # ← відповідає розміру зображення
BOARD_SIZE = 8

LIGHTCOLOR = "#EEEED2"
DARKCOLOR = "#769656"
MIDDLECOLOR = "#769656"

IMAGE_DIR = "classes/images"

root = tk.Tk()
root.title("Chess")

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

frame.pack()
controls.pack(side=tk.BOTTOM, pady=10)

# Оновлюємо кнопки
tk.Button(
    controls,
    text="Reset",
    command=on_reset,
    bg=MIDDLECOLOR,
    fg=LIGHTCOLOR,
    font=("Arial", 14),
    width=12,
    height=2
).pack(side=tk.LEFT, padx=10)

tk.Button(
    controls,
    text="Rotate",
    command=on_rotate,
    bg=MIDDLECOLOR,
    fg=LIGHTCOLOR,
    font=("Arial", 14),
    width=12,
    height=2
).pack(side=tk.LEFT, padx=10)


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

        if (game.board.space[y][x] and self.selected == []) or len(self.selected):
            print(f"Клік: ({x}, {y})")
            self.selected.append((y, x))

            if len(self.selected) == 2:
                src, dst = self.selected
                print(f"Спроба перемістити з {src} до {dst}")
                try:
                    game.move(src, dst)
                    if game.status == "finish":
                        turn = "black" if game.turn == "white" else "white"
                        show_win_window(turn)
                    print("Помилок немає")
                except Exception as e:
                    print("Помилка при ході:", e)
                # game.move(src, dst)
                self.selected = []
                draw_board()
        else:
            print("Клітинка пуста")


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

def show_win_window(player_color):
    win_window = tk.Toplevel(root)
    win_window.title("Game Over")
    win_window.resizable(False, False)

    # Основний фрейм у новому вікні
    container = tk.Frame(win_window, padx=20, pady=20)
    container.pack()

    # Визначаємо текст та іконку
    win_text = f"{player_color.capitalize()} is win"
    icon_name = "wK.png" if player_color == "white" else "bK.png"

    # Завантажуємо зображення
    icon_img = load_image(icon_name)

    # Розміщення елементів
    label = tk.Label(container, text=win_text, font=("Arial", 28, "bold"), fg=DARKCOLOR)
    label.grid(row=0, column=0, padx=10)

    if icon_img:
        icon_label = tk.Label(container, image=icon_img)
        icon_label.image = icon_img  # Зберігаємо посилання
        icon_label.grid(row=0, column=1)


draw_board()
root.mainloop()
