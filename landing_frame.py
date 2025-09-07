from tkinter import *

def create_landing_frame(root, show_frame, stats_entry_frame, stats_viewer_frame):
    frame = Frame(root)
    Label(frame, text="Welcome to Stats-ketball!", font=("Arial", 16)).pack(pady=30)
    Button(frame, text="Enter Stats", width=20, command=lambda: show_frame(stats_entry_frame)).pack(pady=10)
    Button(frame, text="View Stats", width=20, command=lambda: show_frame(stats_viewer_frame)).pack(pady=10)
    Button(frame, text="Exit", width=20, command=root.destroy).pack(pady=10)
    return frame