#Comparison of Flask_Restful and only Flask

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    def get(self): # predefined method GET
        return jsonify({"A message ": "Happy New Year" })
    
class Cube(Resource):
    def get(self, mynumber):
        return jsonify({f"The cube of {mynumber} is" : mynumber**3})
    
api.add_resource(Message, '/')
api.add_resource(Cube, '/<int:mynumber>')

if __name__ == "__main__":
    app.run(debug=True)