from tkinter import *
import csv

def create_stats_viewer_frame(root, show_frame):
    frame = Frame(root)

    Label(frame, text="Saved Stats", font=("Arial", 14)).pack(pady=10)
    stats_list = Listbox(frame, width=40)
    stats_list.pack(pady=5)

    def load_stats():
        stats_list.delete(0, END)
        try:
            with open('stats.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    stats_list.insert(END, f"Points: {row[0]}, Rebounds: {row[1]}, Assists: {row[2]}")
        except FileNotFoundError:
            stats_list.insert(END, "No stats found.")

    Button(frame, text="Reload", command=load_stats).pack()
    Button(frame, text="Home", command=lambda: show_frame('landing')).pack(pady=5)
    Button(frame, text="Enter Stats", command=lambda: show_frame('stats_entry')).pack()

    # Load stats initially
    load_stats()

    return frame