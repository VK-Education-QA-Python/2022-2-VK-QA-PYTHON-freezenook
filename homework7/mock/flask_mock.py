import os
import threading
from flask import Flask, jsonify, request
import settings


app = Flask(__name__)
NUMBERPLATE_DATA = {}


@app.route('/get_numberplate/<car_model>', methods=['GET'])
def get_car_numberplate(car_model):
    if numberplate := NUMBERPLATE_DATA.get(car_model):
        return jsonify(numberplate), 200
    else:
        return jsonify(f'Surname for user "{car_model}" not found'), 404


@app.route('/update_numberplate/<car_model>', methods=['PUT'])
def update_user_numberplate(car_model):
    old_numberplate = NUMBERPLATE_DATA.get(car_model)
    new_numberplate = request.json.get('numberplate')

    if new_numberplate:
        NUMBERPLATE_DATA[car_model] = new_numberplate
        return jsonify(f'Numberplate was updated for "{car_model}": from "{old_numberplate}" to "{new_numberplate}"'), 200
    else:
        return jsonify('New numberplate was not provided'), 400


@app.route('/delete_numberplate/<car_model>', methods=['DELETE'])
def delete_car_numberplate(car_model):
    try:
        removed_numberplate = NUMBERPLATE_DATA.pop(car_model)
        return jsonify(f'Numberplate of "{car_model}" ("{removed_numberplate}") has been removed'), 200
    except KeyError:
        return jsonify(f'Numberplate of "{car_model}" not found'), 404


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()
    else:
        raise RuntimeError('Not running with the Werkzeug Server')


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server


if __name__ == '__main__':
    host = os.environ.get('MOCK_HOST', '127.0.0.1')
    port = os.environ.get('MOCK_PORT', '4444')

    app.run(host, port)
