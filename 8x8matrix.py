import tkinter as tk

# Constants for the matrix size and cell dimensions
MATRIX_SIZE = 8  # 8x8 matrix
CELL_SIZE = 50   # Each cell is 50x50 pixels

# The string to be displayed in the matrix
text = "PHOBICTIKVARTFEMPÅGOVERQHALVDFEMFIRESEKSTOLVSJUXRXÅTTETTELLEVENI"

# Highlight texts and their specific character ranges
# Each tuple contains the highlight text and its (start, end) range
highlight_texts_ranges = [
    ("PHOBIC", (0, 15)),  # Affects characters 0 to 15
    ("PÅ", (16, 23)), # Affects characters 16 to 23
    ("HALV", (24, 31)), # Affects characters 24 to 31
    ("SJU", (28, 63))  # Affects characters 28 to 63
]

# Initialize the Tkinter window
root = tk.Tk()
root.title("8x8 Matrix with Text")

# Create a canvas to draw the matrix
canvas = tk.Canvas(root, width=MATRIX_SIZE * CELL_SIZE, height=MATRIX_SIZE * CELL_SIZE, bg="black")
canvas.pack()

# Function to check if the character at position idx should be highlighted
def should_highlight(idx):
    for highlight_text, (start, end) in highlight_texts_ranges:
        # Check if idx falls within the specified range for this highlight text
        if start <= idx <= end:
            # Check if any part of the highlight_text matches within its range
            text_slice = text[start:end+1]  # +1 because end is inclusive in this context
            if highlight_text in text_slice:
                # Calculate offset of highlight_text within the slice
                highlight_start_idx = text_slice.index(highlight_text)
                highlight_end_idx = highlight_start_idx + len(highlight_text) - 1
                # Check if current idx falls within the highlight_text span in its range
                if highlight_start_idx <= (idx - start) <= highlight_end_idx:
                    return True
    return False

# Function to draw the 8x8 matrix on the canvas with letters
def draw_matrix_with_text():
    for idx, char in enumerate(text):
        i, j = divmod(idx, MATRIX_SIZE)
        x1 = j * CELL_SIZE
        y1 = i * CELL_SIZE
        # Determine text color (highlight if part of any highlight_texts within their ranges)
        text_color = "green" if should_highlight(idx) else "white"
        # Draw the character in the cell
        canvas.create_text(x1 + CELL_SIZE/2, y1 + CELL_SIZE/2, text=char, fill=text_color, font=("Arial", 16))

# Draw the matrix with text
draw_matrix_with_text()

# Run the Tkinter event loop
root.mainloop()
