def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    keep_running=True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
def HDL_value():
    HDL_input=input("Enter HDL value for the patient:")
    return int(HDL_input)
interface()
