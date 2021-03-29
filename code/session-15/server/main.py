import constants

from flask import Flask, request, jsonify
# from flask_restful import Api, Resource

app = Flask(__name__)
# api = Api(app)

# class Hospital(Resource):
    # def get(self):
    #     return {"data": "Get from the hospital"}

    # def post(self):
    #     return {"data": "Posted"}

    # def delete(self):
    #     pass
    
# api.add_resource(Hospital, "/patients")

@app.route('/patients', methods=['GET'])
def patients():
    return jsonify(constants.patients_list)

if __name__ == "__main__":
    app.run(debug=True)
