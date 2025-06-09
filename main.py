# Import Module
from tkinter import *
import csv


# create root window
root = Tk()

# Function to save stats to CSV
def save_stats():
    points = points_entry.get()
    rebounds = rebounds_entry.get()
    assists = assists_entry.get()
    with open('stats.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([points, rebounds, assists])

# root window title and dimension
root.title("Stats-ketball")
# Set geometry (widthxheight)
root.geometry('350x200')


# adding a label to the root window
points_label = Label(root, text = "Points")
points_label.grid(column=0, row=0)

# adding Entry Field
points_entry = Entry(root, width=10)
points_entry.grid(column=1, row=0)

# adding a label to the root window
assists_label = Label(root, text = "Rebounds")
assists_label.grid(column=0, row=1)

# adding Entry Field
rebounds_entry = Entry(root, width=10)
rebounds_entry.grid(column=1, row=1)

# adding a label to the root window
assists_label = Label(root, text = "Assists")
assists_label.grid(column=0, row=2)

# adding Entry Field
assists_entry = Entry(root, width=10)
assists_entry.grid(column=1, row=2)

# Save Button
save_button = Button(root, text="Save stats", command=save_stats)
save_button.grid(column=1, row=3, pady=10)


# all widgets will be here
# Execute Tkinter
root.mainloop()