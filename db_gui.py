import tkinter as tk
from tkinter import ttk
import client
from PIL import Image, ImageTk
from tkinter import filedialog


# Any code that manipulates data should be out of the main_window
# All functions need a docstring! Does not matter where they are located
def create_blood_type(letter, rh):
    output = "{}{}".format(letter, rh)
    return output


def upload_data_to_server(patient_name, patient_id,
                          patient_blood_letter, patient_rh_factor):
    blood_type = create_blood_type(patient_blood_letter, patient_rh_factor)
    patient_id = int(patient_id)
    msg, code = client.upload_patient_info(patient_name,
                                           patient_id,
                                           blood_type)
    return msg


# GUI-related functions will not be tested!
def main_window():

    def get_update_info():
        print("Get data")
        root.after(2000, get_update_info)

    # He will look for usability!
    def ok_cmd():
        # These function should do 3 things
        if rh_button.get() == "":
            print("Chose Rh factor")
            return
        # 1. Get data from interface
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh_factor = rh_button.get()

        # 2. Call other testable functions to do all the work
        msg = upload_data_to_server(patient_name, patient_id, patient_blood_letter,
                              patient_rh_factor)
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient ID: {}".format(patient_id_entry.get()))
        print(" Patient Blood Type: {}{}".format(blood_letter_selection.get(),
                                                 rh_button.get()))
        print("Closest Donation Center: {}".format(donor_center.get()))
        print("Clicked Ok button")
        # 3. Update GUI based on results of other functions
        status_label.configure(text=msg)

    def cancel_cmd():
        print("Clicked Cancel Button")
        root.destroy()  # This function will completely close the GUI

    def picture_button_cmd():
        # new_file = "rat.jpeg"
        # Code will only be tested with .jpeg images
        new_image = filedialog.askopenfilename()
        if new_image == "":
            return
        print("Filename: {}".format(new_image))
        pil_image = Image.open(new_image)
        x_size, y_size = pil_image.size
        new_y = 200
        new_x = new_y * x_size/y_size
        pil_image = pil_image.resize((round(new_x), new_y))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

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

    picture_button = ttk.Button(root, text="Load Picture",
                                command=picture_button_cmd)
    picture_button.grid(column=2, row=8)

    # Drop down box
    # You can both select, and type new
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(row=1, column=2, columnspan=2)
    donor_center_combo["values"] = ["Durham", "Chapel Hill", "Raleigh"]
    # If doing this, you cannot change the values
    donor_center_combo.state(["readonly"])

    status_label = ttk.Label(root, text="Status")
    status_label.grid(column=0, row=7)
    # tkinter.messagebox is a good alternative for this status label
    # It will create a pop-up message for the client

    pil_image = Image.open("stress.jpeg")
    pil_image = pil_image.resize((200,100))
    tk_image = ImageTk.PhotoImage(pil_image)
    # Images are shown in tk bt showing them on Labels (Image Label)
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=1, row=8)
    image_label.image = tk_image

    root.after(2000, get_update_info) # After x ms, run the following function
    root.mainloop()  # Starts the interface, the loop that waits for an event


if __name__ == "__main__":
    main_window()
