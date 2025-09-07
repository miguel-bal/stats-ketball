from tkinter import *
from tkinter import filedialog
import csv

def create_stats_viewer_frame(root, show_frame):
    frame = Frame(root)

    Label(frame, text="View Stats", font=("Arial", 14)).pack(pady=10)

    # Table frame for grid layout
    table_frame = Frame(frame)
    table_frame.pack(pady=5)

    # Function to clear the table
    def clear_table():
        for widget in table_frame.winfo_children():
            widget.destroy()

    def load_file():
        file_path = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        clear_table()
        if file_path:
            try:
                with open(file_path, newline='') as file:
                    reader = csv.reader(file)
                    next(reader, None)  # Skip the header row
                    for row_idx, row in enumerate(reader):
                        if len(row) >= 3:
                            Label(table_frame, text="Points:", anchor="e", width=10).grid(row=row_idx*3, column=0, sticky="e")
                            Label(table_frame, text=row[0], anchor="w", width=20).grid(row=row_idx*3, column=1, sticky="w")
                            Label(table_frame, text="Rebounds:", anchor="e", width=10).grid(row=row_idx*3+1, column=0, sticky="e")
                            Label(table_frame, text=row[1], anchor="w", width=20).grid(row=row_idx*3+1, column=1, sticky="w")
                            Label(table_frame, text="Assists:", anchor="e", width=10).grid(row=row_idx*3+2, column=0, sticky="e")
                            Label(table_frame, text=row[2], anchor="w", width=20).grid(row=row_idx*3+2, column=1, sticky="w")
                        else:
                            Label(table_frame, text="Incomplete row:", anchor="e", width=15).grid(row=row_idx*3, column=0, sticky="e")
                            Label(table_frame, text=str(row), anchor="w", width=30).grid(row=row_idx*3, column=1, sticky="w")
            except Exception as e:
                Label(table_frame, text=f"Error loading file: {e}").grid(row=0, column=0, columnspan=2)
        else:
            Label(table_frame, text="No file selected.").grid(row=0, column=0, columnspan=2)

    Button(frame, text="Load File", command=load_file).pack()
    Button(frame, text="Home", command=lambda: show_frame('landing')).pack(pady=5)
    Button(frame, text="Enter Stats", command=lambda: show_frame('stats_entry')).pack()

    return frame