def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def printing_params(db):
    for patient in db:
        print("Name:{},ID :{},Age{}"
              .format(patient[0], patient[1], patient[2]))


def find_patient(db, id_num):
    for patient in db:
        if patient[1] == id_num:
            print("The patient with this ID is {}"
                  .format(patient[0]))
            return patient
    return False


def test_results(db, id, test_name, test_value):
    test = [test_name, test_value]
    patient = find_patient(db, id)
    patient[3].append(test)
    print(patient)


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    printing_params(db)
    test_results(db, 2, "HDL", "Elevated")
    room_list = ["Room 1", "Room 2", "Room 3"]
    i = 0
    for i, patient in enumerate(db):
        print("Name: {},Room: {}".format(patient[0], room_list[i]))


if __name__ == "__main__":
    main()
