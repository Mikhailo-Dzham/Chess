# proto_visualizator.py
import tkinter as tk

CELL_SIZE = 60
BOARD_SIZE = 8
CIRCLE_RADIUS = 20

root = tk.Tk()
root.title("Шахи")
canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE)
canvas.pack()

def draw_chessboard():
    colors = ("#EEEED2", "#769656")  # Світлі та темні клітинки
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

def draw_circle_in_cell(col, row, color="red"):
    x_center = col * CELL_SIZE + CELL_SIZE // 2
    y_center = row * CELL_SIZE + CELL_SIZE // 2
    x1 = x_center - CIRCLE_RADIUS
    y1 = y_center - CIRCLE_RADIUS
    x2 = x_center + CIRCLE_RADIUS
    y2 = y_center + CIRCLE_RADIUS
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

class CircleDrawer:
    def clear(self):
        # Видаляємо всі об'єкти, крім прямокутників та тексту (тобто не стираємо дошку та координати)
        for item in canvas.find_all():
            tags = canvas.gettags(item)
            if canvas.type(item) == "oval":
                canvas.delete(item)

circle_drawer = CircleDrawer()
