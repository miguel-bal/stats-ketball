from tkinter import *
from tkinter import filedialog
import csv

def create_stats_viewer_frame(root, show_frame):
    frame = Frame(root)
    inner = Frame(frame)
    inner.place(relx=0.5, rely=0.5, anchor='center')

    Label(inner, text="View Average Stats", font=("Arial", 14)).pack(pady=10)

    # Table frame for grid layout
    table_frame = Frame(inner)
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
                    points_sum = 0
                    rebounds_sum = 0
                    assists_sum = 0
                    count = 0
                    for row in reader:
                        if len(row) >= 3:
                            try:
                                points_sum += float(row[0])
                                rebounds_sum += float(row[1])
                                assists_sum += float(row[2])
                                count += 1
                            except ValueError:
                                continue  # Skip rows with non-numeric data
                    if count > 0:
                        avg_points = points_sum / count
                        avg_rebounds = rebounds_sum / count
                        avg_assists = assists_sum / count
                        Label(table_frame, text="Points:", anchor="e", width=15).grid(row=0, column=0, sticky="e")
                        Label(table_frame, text=f"{avg_points:.2f}", anchor="w", width=20).grid(row=0, column=1, sticky="w")
                        Label(table_frame, text="Rebounds:", anchor="e", width=15).grid(row=1, column=0, sticky="e")
                        Label(table_frame, text=f"{avg_rebounds:.2f}", anchor="w", width=20).grid(row=1, column=1, sticky="w")
                        Label(table_frame, text="Assists:", anchor="e", width=15).grid(row=2, column=0, sticky="e")
                        Label(table_frame, text=f"{avg_assists:.2f}", anchor="w", width=20).grid(row=2, column=1, sticky="w")
                    else:
                        Label(table_frame, text="No valid data found.").grid(row=0, column=0, columnspan=2)
            except Exception as e:
                Label(table_frame, text=f"Error loading file: {e}").grid(row=0, column=0, columnspan=2)
        else:
            Label(table_frame, text="No file selected.").grid(row=0, column=0, columnspan=2)

    Button(inner, text="Load File", command=load_file).pack()
    Button(inner, text="Home", command=lambda: show_frame('landing')).pack(pady=5)
    Button(inner, text="Enter Stats", command=lambda: show_frame('stats_entry')).pack()

    return frame
