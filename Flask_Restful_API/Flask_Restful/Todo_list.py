from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class FirstPage(Resource):
    def get(self):
        return {"Welcome to" : "Our Flask Testing Environment",
                "Pick Your Number" : [1,2,3,4]}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
        # if todo_id in todos:
        #     return {todo_id: todos[todo_id]}
        # else:
        #     return {"message" : "Todo item not found"}, 404

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(FirstPage, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)