import pytest
from db_definition import Patient


def test_add_patient():
        from db_server import add_patient, init_server
        init_server()
        patient_name = "David"
        patient_id = 222
        blood_type = "A+"
        answer = add_patient(patient_name, patient_id, blood_type)
        # I should delete this new entry from my database so that it stays the
        # same after the test
        find_patient = Patient.objects.raw({"_id": 222}).first()
        find_patient.delete()
        assert answer.name == patient_name

        # Set up the data base
        # Run code with what you want to test
        # Clean up database


def test_add_test_to_patient():
        from db_server import init_server, add_patient, add_test_to_patient
        patient_id = 123
        patient_name = "Rocio"
        blood_type = "A+"
        added_patient = add_patient(patient_name, patient_id, blood_type)

        test_name = "XXX"
        test_result = 200
        out_data = {"id": patient_id,
                    "test_name": test_name,
                    "test_result": test_result}
        answer = add_test_to_patient(out_data)
        patient_from_db = Patient.object.raw({"_id": patient_id}).first()

        added_patient.delete()

        assert patient_from_db.test_name[-1] == test_name
        assert patient_from_db.test_result[-1] == test_result
