import tkinter as tk
from tkinter import ttk


def main_window():
    # Will do everything related to main interface
    root = tk.Tk()  # This creates the root/most basic window
    root.title("Blood Donor Database")  # Give a title to the window
    root.geometry("600x300")
    root.columnconfigure(1, minsize=100)
    root.columnconfigure(2, minsize=100)

    ttk.Label(root, text="Blood Donor Database").grid(row=0, column=0,
                                                      columnspan=2)
    # First variable= parent variable, text= what text you want to display
    # .grid() to tell where it should go
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    ttk.Label(root, text="ID:").grid(column=0, row=2)
    ttk.Label(root, text="Closest Donation Center").grid(row=0, column=2,
                                                         columnspan=2)

    ttk.Entry(root, width=25).grid(column=1, row=1)
    ttk.Entry(root, width=25).grid(column=1, row=2)



    root.mainloop()  # Starts the interface, the loop that waits for an event


if __name__ == "__main__":
    main_window()
