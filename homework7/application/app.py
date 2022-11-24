import os
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)

app_data = {}
car_id_seq = 1


@app.route('/add_car', methods=['POST'])
def add_new_car():
    global car_id_seq

    car_model = request.json['car_model']
    if car_model not in app_data:
        app_data[car_model] = car_id_seq
        car_id_seq += 1
        return jsonify({'car_id': app_data[car_model]}), 201

    else:
        return jsonify(f'Car {car_model} already exists with id {app_data[car_model]}'), 400


@app.route('/delete_car', methods=['DELETE'])
def delete_car():
    car_model = request.json['car_model']
    if car_model not in app_data:
        return jsonify(f'Car {car_model} not found'), 404
    else:
        app_data.pop(car_model)
        return jsonify(f'Car {car_model} has been removed'), 200


@app.route('/get_car/<car_model>', methods=['GET'])
def get_car_id_by_model(car_model):
    car_id = app_data.get(car_model)
    if car_id:
        age_host = os.environ['STUB_HOST']
        age_port = os.environ['STUB_PORT']

        age = None
        try:
            age = requests.get(f'http://{age_host}:{age_port}/get_age/{car_model}').json()
        except Exception as e:
            print(f'Unable to get age from external system 1:\n{e}')

        numberplate_host = os.environ['MOCK_HOST']
        numberplate_port = os.environ['MOCK_PORT']

        numberplate = None
        try:
            response = requests.get(f'http://{numberplate_host}:{numberplate_port}/get_numberplate/{car_model}')
            if response.status_code == 200:
                numberplate = response.json()
            else:
                print(f'No numberplate {car_model}')
        except Exception as e:
            print(f'Unable to get surname from external system 2:\n{e}')

        data = {'car_id': car_id,
                'age': age,
                'numberplate': numberplate
                }
        return jsonify(data), 200
    else:
        return jsonify(f'Car {car_model} not found'), 404


@app.route('/update_numberplate/<car_model>', methods=['PUT'])
def update_numberplate(car_model):
    numberplate_host = os.environ['MOCK_HOST']
    numberplate_port = os.environ['MOCK_PORT']
    resp = requests.put(f'http://{numberplate_host}:{numberplate_port}/update_numberplate/{car_model}', json=request.get_json())
    return jsonify(resp.content.decode()), resp.status_code


@app.route('/delete_numberplate/<name>', methods=['DELETE'])
def delete_numberplate(name):
    numberplate_host = os.environ['MOCK_HOST']
    numberplate_port = os.environ['MOCK_PORT']
    resp = requests.delete(f'http://{numberplate_host}:{numberplate_port}/delete_numberplate/{name}')
    return jsonify(resp.content.decode()), resp.status_code


if __name__ == '__main__':
    host = os.environ.get('APP_HOST', '127.0.0.1')
    port = os.environ.get('APP_PORT', '4444')

    app.run(host, port)
