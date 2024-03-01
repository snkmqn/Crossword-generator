import tkinter as tk
from tkinter import ttk

def generate_crossword():
    root = tk.Tk()
    root.title('Crossword Generator')

    words = {}

    def add_word():
        word = entry_word.get()
        orientation = entry_orientation.get()
        start_row_str = entry_start_row.get()
        start_col_str = entry_start_col.get()

        if not (word and orientation and start_row_str and start_col_str):
            print('Please, enter all required fields.')
            return

        start_row = int(start_row_str)
        start_col = int(start_col_str)

        words[word] = {'orientation': orientation, 'start_row': start_row, 'start_col': start_col}

        entry_word.delete(0, tk.END)
        entry_orientation.delete(0, tk.END)
        entry_start_row.delete(0, tk.END)
        entry_start_col.delete(0, tk.END)

    def generate():
        if not words:
            print('The dictionary of words is empty. Impossible to create the crossword.')
            return

        root.destroy()
        generate_crossword_with_layout(words)

    tk.Label(root, text='Word:').grid(row=0, column=0)
    tk.Label(root, text='Orientation (horizontal/vertical):').grid(row=1, column=0)
    tk.Label(root, text='Start Row:').grid(row=2, column=0)
    tk.Label(root, text='Start Col:').grid(row=3, column=0)

    entry_word = tk.Entry(root)
    entry_orientation = tk.Entry(root)
    entry_start_row = tk.Entry(root)
    entry_start_col = tk.Entry(root)

    entry_word.grid(row=0, column=1)
    entry_orientation.grid(row=1, column=1)
    entry_start_row.grid(row=2, column=1)
    entry_start_col.grid(row=3, column=1)

    tk.Button(root, text='Add Word', command=add_word).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(root, text='Generate Crossword', command=generate).grid(row=5, column=0, columnspan=2)

    root.mainloop()

def generate_crossword_with_layout(words):
    if not words:
        return ('The dictionary of words is empty. Impossible to create the crossword.')

    max_word_length = max(len(word) for word in words.keys())
    grid_size = max_word_length + 2

    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Sample definitions for words
    definitions = {
        'python': 'A high-level, interpreted programming language.',
        'program': 'A set of instructions that can be executed by a computer.',
        'optimization': 'A process of maximization of profitable characteristics or ratios.'
    }

    root = tk.Tk()
    root.title('Crossword')

    canvas = tk.Canvas(root, width=grid_size * 40, height=grid_size * 40)
    canvas.grid(row=0, column=0, padx=10, pady=10)

    tree = ttk.Treeview(root, columns=('Coordinates', 'Orientation', 'Definition'), show='headings')
    tree.heading('Coordinates', text='Coordinates')
    tree.heading('Orientation', text='Orientation')
    tree.heading('Definition', text='Definition')

    tree.column('Coordinates', width=80, anchor='center')
    tree.column('Orientation', width=80, anchor='center')
    tree.column('Definition', width=400, anchor='w')

    tree.grid(row=0, column=1, padx=10, pady=10)

    for word, info in words.items():
        orientation = info['orientation']
        start_row, start_col = info['start_row'], info['start_col']

        coordinates = f"({start_row + 1}, {start_col + 1})"
        definition = definitions.get(word, 'Definition not found.')

        tree.insert('', tk.END, values=(coordinates, orientation, definition))

        if orientation == 'horizontal':
            for i in range(len(word)):
                if 0 <= start_row < grid_size and 0 <= start_col + i < grid_size:
                    grid[start_row][start_col + i] = word[i]
        elif orientation == 'vertical':
            for i in range(len(word)):
                if 0 <= start_row + i < grid_size and 0 <= start_col < grid_size:
                    grid[start_row + i][start_col] = word[i]

    for row in range(grid_size):
        for col in range(grid_size):
            x0, y0 = col * 40, row * 40
            x1, y1 = (col + 1) * 40, (row + 1) * 40

            if grid[row][col] == ' ':
                canvas.create_rectangle(x0, y0, x1, y1, fill='black')
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill='white')

    root.mainloop()

generate_crossword()
