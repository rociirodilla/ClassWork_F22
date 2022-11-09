import tkinter as tk
from tkinter import ttk


def main_window():
    # He will look for usability!
    def ok_cmd():
        if rh_button.get() == "":
            print("Chose Rh factor")
            return
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient ID: {}".format(patient_id_entry.get()))
        print(" Patient Blood Type: {}{}".format(blood_letter_selection.get(),
                                                 rh_button.get()))
        print("Closest Donation Center: {}".format(donor_center.get()))
        print("Clicked Ok button")

    def cancel_cmd():
        print("Clicked Cancel Button")
        root.destroy()  # This function will completely close the GUI

    # Will do everything related to main interface
    root = tk.Tk()  # This creates the root/most basic window
    root.title("Blood Donor Database")  # Give a title to the window
    # root.geometry("600x300")
    root.columnconfigure(1, minsize=50)
    root.columnconfigure(2, minsize=50)

    ttk.Label(root, text="Blood Donor Database").grid(row=0, column=0,
                                                      columnspan=2, sticky="w") # or sticky tk.NW...
    # First variable= parent variable, text= what text you want to display
    # .grid() to tell where it should go
    # Create labels
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky=tk.E)
    ttk.Label(root, text="Closest Donation Center").grid(row=0, column=2,
                                                         columnspan=2)

    patient_name_entry = tk.StringVar()  # Creates a string
    #  tk.IntVar()  # Creates an integer
    patient_id_entry = tk.StringVar()
    # Create a box that receives an input, and saves it to the defined variable
    ttk.Entry(root, width=25, textvariable=patient_name_entry).grid(column=1, row=1)
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1, row=2, sticky=tk.W)

    # Create a button
    # state=tk.DISABLED will disable the button
    # In the command, do not use the function as function() but as function,
    # if not, it will run even tho you have not clicked the button
    ttk.Button(root, text="OK", command=ok_cmd).grid(column=1, row=6,
                                                     columnspan=2)
    ttk.Button(root, text='Cancel', command=cancel_cmd).grid(column=2, row=6,
                                                             columnspan=2)

    blood_letter_selection = tk.StringVar()
    # Fot the radio buttons, you have to select a variable and then the value. The value
    # Does not have to be the same as the text!
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3, sticky="w")
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4, sticky="w")
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5, sticky="w")
    ttk.Radiobutton(root, text="0", variable=blood_letter_selection,
                    value="0").grid(column=0, row=6, sticky="W")

    # rh_button = tk.BooleanVar()  Boolean variable
    rh_button = tk.StringVar()
    # For a checkbox; on- and offvalue will determine the value of the string
    ttk.Checkbutton(root, text="Rh positive", variable=rh_button,
                    onvalue="+", offvalue="-").grid(column=1, row=4)

    # Drop down box
    # You can both select, and type new
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(row=1, column=2, columnspan=2)
    donor_center_combo["values"] = ["Durham", "Chapel Hill", "Raleigh"]
    # If doing this, you cannot change the values
    donor_center_combo.state(["readonly"])

    root.mainloop()  # Starts the interface, the loop that waits for an event


if __name__ == "__main__":
    main_window()
