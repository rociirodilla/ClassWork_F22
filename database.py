def create_patient_entry(patient_first, patient_last, patient_id, patient_age):
    new_patient = {"First Name":patient_first,
                   "Last Name": patient_last,
                   "ID":patient_id,
                   "Age": patient_age,
                   "Test": []}
    return new_patient


def full_name(patient):
    full_name= "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name
    
    
def printing_params(db):
    for patient in db:
        print(patient)
        print("Name:{},ID :{},Age{}".format(full_name(db[patient]),db[patient]["ID"], db[patient]["Age"]))


def find_patient(db, id_num):
    patient=db[id_num]
    return patient

def test_results(db, id, test_name, test_value):
    test = [test_name, test_value]
    patient = find_patient(db, id)
    patient["Test"].append(test)
    print(patient)


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"

def main():
    db = {}
    db[11]=create_patient_entry("Ann", "Ables", 11, 30)
    db[22]=create_patient_entry("Bob", "Boyles", 22, 34)
    db[3]=create_patient_entry("Chris", "Chou", 3, 25)
    #print(db)
    printing_params(db)
    test_results(db, 3, "HDL", 100)
    printing_params(db)
    #print("Patient {} is a {}".format(full_name(db[2]),adult_or_minor(db[2])))
   
   
if __name__ == "__main__":
    main()
