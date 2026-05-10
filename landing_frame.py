from tkinter import Frame, Label, Button

def create_landing_frame(root, show_frame):
    frame = Frame(root)
    inner = Frame(frame)
    inner.place(relx=0.5, rely=0.5, anchor='center')
    Label(inner, text="Welcome to Stats-ketball!", font=("Arial", 16)).pack(pady=30)
    Button(inner, text="Enter Stats", width=20, command=lambda: show_frame('stats_entry')).pack(pady=10)
    Button(inner, text="View Stats", width=20, command=lambda: show_frame('stats_viewer')).pack(pady=10)
    Button(inner, text="Exit", width=20, command=root.destroy).pack(pady=10)
    return frame
