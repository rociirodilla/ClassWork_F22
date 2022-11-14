# client.py
# You can enter requests from your server and through code
import requests


# requests does not call the function but the route!
# out_data = {"name": "Rocio Rodriguez",
#             "hdl_value": 50}
# r = requests.post("http://127.0.0.1:5000/hdl_check", json=out_data)
# print(r.status_code)
# print(r.text)

# For get requests, we only need the url
# For post request, url needed as well as data

# out_data = {"a": 50,
#             "b": 11}
# r = requests.post("http://127.0.0.1:5000/add_numbers", json=out_data)
# print(r.status_code)
# print(r.text)
# answer = r.json()
# a = answer + 3
# print(a)


# r = requests.get("http://127.0.0.1:5000/add/2/3")
# print(r.status_code)
# print(r.text)

# test_data = {"id": 1, "test_name": "LDL", "test_result": 100}

def upload_patient_info(patient_name, patient_id, patient_blood_type):
    out_data = {"name": patient_name,
                "id": patient_id,
                "blood_type": patient_blood_type}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
    return r.text, r.status_code
