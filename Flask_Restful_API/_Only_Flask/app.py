#Comparison of Flask_Restful and only Flask

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def mymethod():
    if (request.method == 'GET'):
        data = "Happy New Year"
        print("Hello World")
        return jsonify({"A message" : data })
    
@app.route('/<int:mynumb>', methods = ['GET'])
def cube(mynumb):
    return jsonify({f"The cube number of {mynumb}" : mynumb**3, 
                    f"The {mynumb**3} divides by 12 is your salary per month(You wish)" : (mynumb**3)/12})

if __name__ == "__main__":
    app.run(debug=True)