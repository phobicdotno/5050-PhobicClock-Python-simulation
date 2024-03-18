import tkinter as tk

# Constants for the matrix size and cell dimensions
MATRIX_SIZE = 8  # 8x8 matrix
CELL_SIZE = 50   # Each cell is 50x50 pixels

# Initialize the Tkinter window
root = tk.Tk()
root.title("8x8 Matrix")

# Create a canvas to draw the matrix
canvas = tk.Canvas(root, width=MATRIX_SIZE * CELL_SIZE, height=MATRIX_SIZE * CELL_SIZE, bg="white")
canvas.pack()

# Function to draw the 8x8 matrix on the canvas
def draw_matrix():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")

# Draw the matrix
draw_matrix()

# Run the Tkinter event loop
root.mainloop()
