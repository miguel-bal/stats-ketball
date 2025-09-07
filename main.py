# Import Module
from tkinter import *
import csv
from landing_frame import create_landing_frame
from stats_entry_frame import create_stats_entry_frame
from stats_viewer_frame import create_stats_viewer_frame


root = Tk()
root.title("Stats-ketball")
root.resizable(False, False)

def show_frame(frame_name):
    frames[frame_name].tkraise()

# Create all frames and store them in a dictionary
frames = {}

frames['stats_entry'] = create_stats_entry_frame(root, show_frame)
frames['stats_viewer'] = create_stats_viewer_frame(root, show_frame)
frames['landing'] = create_landing_frame(root, show_frame)

# Add all frames to the grid
for frame in frames.values():
    frame.grid(row=0, column=0, sticky='nsew')

# Show the landing frame first
show_frame('landing')

# Execute Tkinter
root.mainloop()