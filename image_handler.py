import base64
from tkinter import filedialog
import requests


def upload_image(net_id, id_no):
    filename = get_image_filename()
    b64_string = convert_file_to_b64(filename)
    status_code, result = upload_b64_to_server(b64_string,
                                               net_id,
                                               id_no)
    return status_code, result


def get_image_filename():
    filename = filedialog.askopenfilename()
    # filename = "rat.jpeg"
    return filename


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes,
                     encoding='utf-8')
    return b64_string


def upload_b64_to_server(b64_string, net_id, id_no):
    out = {"image": b64_string,
           "net_id": net_id,
           "id_no": id_no}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image",
                      json=out)
    return r.status_code, r.text


def retrieve_image():
    b64_string = get_image_from_server()
    save_b64_to_file(b64_string)


def get_image_from_server():
    r = requests.get("http://vcm-21170.vm.duke.edu/get_image/mr463/1")
    b64_string = r.text
    return b64_string


def save_b64_to_file(b64_string):
    new_filename = "rat_watermark.jpg"
    image_bytes = base64.b64decode(b64_string)
    with open(new_filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == "__main__":
    status_code, result = upload_image("mr463", 1)
    print(result)
    retrieve_image()

# Take the image from GIU, convert (in GUI),
# send to server, and store it in the db(from server)
