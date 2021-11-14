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


@app.route('/get_by_name/<name>', methods=['GET'])
def get_by_name(name):
    return name


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


@app.route('/post', methods=['POST'])
def post():
    inputs = request.get_json()
    needs_inputs = ['x', 'y']
    answer = 1
    for _n in needs_inputs:
        if _n in inputs:
            if type(inputs[_n]) == str and inputs[_n].isdigit():
                inputs[_n] = int(inputs[_n])
            elif type(inputs[_n]) != int:
                response = make_response(jsonify(
                    errors=True,
                    exception='Inputs must be in integer',
                    answer='',
                ), 400)
                return response
        else:
            response = make_response(jsonify(
                errors=True,
                exception=f'Bad args, need: {needs_inputs}',
                answer='',
            ), 400)
            return response
        answer *= inputs[_n]
    response = make_response(jsonify(
        errors=False,
        exception='',
        answer=answer,
    ), 200)
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=80)
