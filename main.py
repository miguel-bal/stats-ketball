# Import Module
from tkinter import *

# create root window
root = Tk()

# Function to update points
def update_stats():
    try:
        points = int(txt.get())
        pts_lbl.config(text=f"Points: {points}")
    except ValueError:
        pts_lbl.config(text="Invalid input")

# root window title and dimension
root.title("Stats-ketball")
# Set geometry (widthxheight)
root.geometry('350x200')


# adding a label to the root window
lbl = Label(root, text = "Points")
lbl.grid(column=0, row=0)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

# adding a label to the root window
lbl = Label(root, text = "Rebounds")
lbl.grid(column=0, row=1)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=1)

# adding a label to the root window
lbl = Label(root, text = "Assists")
lbl.grid(column=0, row=2)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=2)


pts_lbl = Label(root, text = "0")
pts_lbl.grid(column=3, row=0)

# all widgets will be here
# Execute Tkinter
root.mainloop()