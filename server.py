# server.py
# Previously installed flask in venv
from flask import Flask, request, jsonify
# no confundirse con requests


app = Flask(__name__)

# If request comes in with slash, the function that follows is
# the one that starts running
@app.route("/", methods=["GET"])
def server_status():
        return "Server is on."


@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculate blood cholesterol levels.\n"
    x += "It is written by Rocio Rodriguez."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_intertet():
    """
        incoming_json = {"name": <name_str>,
                         "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The received value was {}".format(hdl_value))
    # We are not returning this print statement, therefore the client will not be seen,
    # only the server will print it for the developer
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def add_numbers():
    """
    incoming_json = {"a": <num1_int>,
                     "b": <num2_int>}
    """
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    # We can not return integers, only strings, lists, dictionaries or tuples
    return jsonify(answer)
# If you jsonify, does not matter what type of data we are using.

if __name__ == "__main__":
    app.run()
