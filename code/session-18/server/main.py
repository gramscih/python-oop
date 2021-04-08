import constants

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/patients", methods=['GET'])
def patients():
    return jsonify(constants.patients_list)

if __name__ == "__main__":
    app.run(debug=True)