import tkinter as tk

CELL_SIZE = 80
BOARD_SIZE = 8
CIRCLE_RADIUS = 20
LIGHTCOLOR = "#EEEED2"
DARKCOLOR = "#769656"


root = tk.Tk()
root.title("Шахи")
canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE)
canvas.pack()

def draw_chessboard():
    colors = (LIGHTCOLOR, DARKCOLOR )  # Світлі та темні клітинки
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = colors[(row + col) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    # Додаємо індекси (a-h, 1-8)
    for i in range(BOARD_SIZE):
        canvas.create_text(5, i * CELL_SIZE + CELL_SIZE // 2, anchor="w", text=str(8 - i), font=("Arial", 10, "bold"))
        canvas.create_text(i * CELL_SIZE + CELL_SIZE // 2, BOARD_SIZE * CELL_SIZE - 5, anchor="s", text=chr(97 + i), font=("Arial", 10, "bold"))

tk.mainloop()
