from tkinter import *
from tkinter import filedialog
import csv

def create_stats_entry_frame(root, show_frame):
    frame = Frame(root)

    Label(frame, text="Enter Player Stats", font=("Arial", 14)).grid(column=0, row=0, columnspan=2, pady=10)

    Label(frame, text="Points").grid(column=0, row=1, sticky='e')
    points_entry = Entry(frame, width=10)
    points_entry.grid(column=1, row=1)

    Label(frame, text="Rebounds").grid(column=0, row=2, sticky='e')
    rebounds_entry = Entry(frame, width=10)
    rebounds_entry.grid(column=1, row=2)

    Label(frame, text="Assists").grid(column=0, row=3, sticky='e')
    assists_entry = Entry(frame, width=10)
    assists_entry.grid(column=1, row=3)

    # Variable to store the currently loaded file path
    loaded_file = {'path': 'stats.csv'}

    def load_stats_file():
        file_path = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if file_path:
            loaded_file['path'] = file_path

    def save_stats():
        points = points_entry.get().strip()
        rebounds = rebounds_entry.get().strip()
        assists = assists_entry.get().strip()
        with open(loaded_file['path'], mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([points, rebounds, assists])
        points_entry.delete(0, END)
        rebounds_entry.delete(0, END)
        assists_entry.delete(0, END)

    Button(frame, text="Load Existing File", command=load_stats_file).grid(column=0, row=4, pady=10)
    Button(frame, text="Save Stats", command=save_stats).grid(column=1, row=4, pady=10)
    Button(frame, text="Home", command=lambda: show_frame('landing')).grid(column=1, row=5, pady=5)

    return frame