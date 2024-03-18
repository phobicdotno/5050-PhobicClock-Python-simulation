import tkinter as tk

# Constants for the matrix size and cell dimensions
MATRIX_SIZE = 8  # 8x8 matrix
CELL_SIZE = 50   # Each cell is 50x50 pixels

# The string to be displayed in the matrix
text = "PHOBICTIKVARTFEMPÅGOVERQHALVDFEMFIRESEKSTOLVSJUXRXÅTTETTELLEVENI"

# List of substrings to highlight, add or remove as needed
highlight_texts = ["TI", "PÅ", "HALV", "FEM"]  # Example highlight texts

# Ensure the text length matches the matrix size
if len(text) != MATRIX_SIZE * MATRIX_SIZE:
    raise ValueError("The text length does not match the matrix size (64 characters needed).")

# Initialize the Tkinter window
root = tk.Tk()
root.title("8x8 Matrix with Text")

# Create a canvas to draw the matrix
canvas = tk.Canvas(root, width=MATRIX_SIZE * CELL_SIZE, height=MATRIX_SIZE * CELL_SIZE, bg="black")
canvas.pack()

# Function to check if the character at position idx should be highlighted based on multiple highlight texts
def should_highlight(idx):
    for highlight_text in highlight_texts:
        if highlight_text:  # Ensure the highlight_text is not empty
            for start_idx in range(max(0, idx - len(highlight_text) + 1), idx + 1):
                if text[start_idx:start_idx + len(highlight_text)] == highlight_text:
                    return True
    return False

# Function to draw the 8x8 matrix on the canvas with letters
def draw_matrix_with_text():
    for idx, char in enumerate(text):
        i, j = divmod(idx, MATRIX_SIZE)
        x1 = j * CELL_SIZE
        y1 = i * CELL_SIZE
        # Determine text color (highlight if part of any highlight_texts)
        text_color = "green" if should_highlight(idx) else "white"
        # Draw the character in the cell
        canvas.create_text(x1 + CELL_SIZE/2, y1 + CELL_SIZE/2, text=char, fill=text_color, font=("Arial", 16))

# Draw the matrix with text
draw_matrix_with_text()

# Run the Tkinter event loop
root.mainloop()
