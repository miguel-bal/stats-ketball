from tkinter import *
from tkinter import filedialog, messagebox
import csv

def create_stats_entry_frame(root, show_frame):
    frame = Frame(root)

    Label(frame, text="Enter Player Stats", font=("Arial", 14)).grid(column=0, row=0, columnspan=3, pady=10)

    # Subtitle label for status
    status_var = StringVar()
    status_var.set("Creating new file: stats.csv")
    status_label = Label(frame, textvariable=status_var, font=("Arial", 10), fg="gray")
    status_label.grid(column=0, row=1, columnspan=3, pady=(0, 10))

    Label(frame, text="Points").grid(column=0, row=2, sticky='e')
    points_entry = Entry(frame, width=10)
    points_entry.grid(column=1, row=2)

    Label(frame, text="Rebounds").grid(column=0, row=3, sticky='e')
    rebounds_entry = Entry(frame, width=10)
    rebounds_entry.grid(column=1, row=3)

    Label(frame, text="Assists").grid(column=0, row=4, sticky='e')
    assists_entry = Entry(frame, width=10)
    assists_entry.grid(column=1, row=4)

    # Variable to store the currently loaded file path
    loaded_file = {'path': 'stats.csv'}

    def load_stats_file():
        file_path = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if file_path:
            loaded_file['path'] = file_path
            status_var.set(f"Loaded file: {file_path.split('/')[-1]}")
        else:
            status_var.set("Creating new file: stats.csv")

    def save_stats():
        points = points_entry.get().strip()
        rebounds = rebounds_entry.get().strip()
        assists = assists_entry.get().strip()
        if not points or not rebounds or not assists:
            messagebox.showerror("Input Error", "All fields must be filled in before saving.")
            return
        if not points.isdigit() or not rebounds.isdigit() or not assists.isdigit():
            messagebox.showerror("Input Error", "All fields must be numeric values.")
            return
        with open(loaded_file['path'], mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([points, rebounds, assists])
        points_entry.delete(0, END)
        rebounds_entry.delete(0, END)
        assists_entry.delete(0, END)
    
    Button(frame, text="Create New File", command=lambda: status_var.set("Creating new file: stats.csv")).grid(column=1, row=6, pady=10)
    Button(frame, text="Load Existing File", command=load_stats_file).grid(column=1, row=7, pady=10)
    Button(frame, text="Save Stats", command=save_stats).grid(column=1, row=8, pady=10)
    Button(frame, text="Home", command=lambda: show_frame('landing')).grid(column=1, row=9, pady=5)

    return frame