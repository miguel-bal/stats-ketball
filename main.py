# Import Module
from tkinter import *
import csv
from landing_frame import create_landing_frame
from stats_entry_frame import create_stats_entry_frame
from stats_viewer_frame import create_stats_viewer_frame


root = Tk()
root.title("Stats-ketball")


def show_frame(frame):
    frame.tkraise()

# Create frames
stats_entry_frame = Frame(root)
stats_viewer_frame = Frame(root)
landing_frame = create_landing_frame(root, show_frame, stats_entry_frame, stats_viewer_frame)
stats_entry_frame = create_stats_entry_frame(root, show_frame, landing_frame, stats_viewer_frame)
stats_viewer_frame = create_stats_viewer_frame(root, show_frame, landing_frame, stats_entry_frame)

for frame in (landing_frame, stats_entry_frame, stats_viewer_frame):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(landing_frame)

# Execute Tkinter
root.mainloop()