import tkinter as tk

# Constants for the matrix size and cell dimensions
MATRIX_SIZE = 8  # 8x8 matrix
CELL_SIZE = 50   # Each cell is 50x50 pixels

# The string to be displayed in the matrix
text = "PHOBICTIKVARTFEMPÅGOVERQHLAVDFEMFIRESEKSTOLVSJUXRXÅTTETTELLEVENI"

# Ensure the text length matches the matrix size
if len(text) != MATRIX_SIZE * MATRIX_SIZE:
    raise ValueError("The text length does not match the matrix size (64 characters needed).")

# Initialize the Tkinter window
root = tk.Tk()
root.title("8x8 Matrix with Inverted Colors")

# Create a canvas to draw the matrix
canvas = tk.Canvas(root, width=MATRIX_SIZE * CELL_SIZE, height=MATRIX_SIZE * CELL_SIZE, bg="black")
canvas.pack()

# Function to draw the 8x8 matrix on the canvas with letters and inverted colors
def draw_matrix_with_text():
    idx = 0  # Index to track the current character in the text
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            # Draw the cell with a black background
            canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill="black")
            # Place the character in the center of the cell with white text
            canvas.create_text(x1 + CELL_SIZE/2, y1 + CELL_SIZE/2, text=text[idx], fill="white", font=("Arial", 16))
            idx += 1

# Draw the matrix with text and inverted colors
draw_matrix_with_text()

# Run the Tkinter event loop
root.mainloop()
