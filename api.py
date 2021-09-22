from flask import Flask, make_response, jsonify, request
from datetime import datetime

app = Flask(__name__)

people = {}


@app.route('/', methods=['GET'])
def index():
    return 'Index page'


@app.route('/headers', methods=['GET'])
def headers():
    response = make_response(jsonify(
        info='info',
        age=21,
        values=['green', 'lemon']
    ), 200)
    response.headers['Date'] = datetime.now()
    response.headers['Some-Info'] = 'some info'
    return response


@app.route('/params/<name>/<age>', methods=['GET'])
def params(name, age):
    response = make_response(jsonify(
        name=name,
        age=age,
        birthday=datetime.now().year - int(age)
    ), 200)
    return response


@app.route('/put/<name>', methods=['PUT'])
def put(name):
    response = make_response('', 204)
    people[name] = request.get_json()['age']
    return response


@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    if name in people:
        del people[name]
        response = make_response('', 204)
    else:
        response = make_response('Unknow name', 404)
    return response



if __name__ == '__main__':
    app.run(host='localhost', port=80)