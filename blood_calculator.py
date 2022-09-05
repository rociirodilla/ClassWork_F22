def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("9 - Quit")
    keep_running=True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
def HDL_value():
    HDL_input=input("Enter HDL value for the patient:")
    return int(HDL_input)
    
def check_HDL(HDL_input):
    if HDL_input >=60:
        return "Normal"
    elif HDL_input < 40:
        return "Low"
    else:
        return "Borderline Low"
    
def HDL_driver():
    Hdl_value=HDL_value()
    answer= check_HDL(Hdl_value)
    output_HDL_result(Hdl_value,answer)
    
def output_HDL_result(hdl_value,charac):
    print("The results for an HDL value of {} is {}.".format(hdl_value,charac))
    
def LDL_value():
    LDL_input=input("Enter LDL value for the patient:")
    return int(LDL_input)

def check_LDL(LDL_input):
    if LDL_input < 130:
        return "Normal"
    elif LDL_input < 150:
        return "Borderline High"
    elif LDL_input <=189:
        return "High"
    else:
        return "Very High"

def LDL_driver():
    Ldl_value=LDL_value()
    answer=check_LDL(Ldl_value)
    output_LDL_result(Ldl_value,answer)

def output_LDL_result(ldl_value,answer):
    print("The results for an LDL value of {} is {}.".format(ldl_value,answer))
    
    
interface()
