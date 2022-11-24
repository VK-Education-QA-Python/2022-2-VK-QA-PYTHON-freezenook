import os
import random
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_age/<car_model>', methods=['GET'])
def get_user_age(car_model):
    return jsonify(random.randint(1980, 2023)), 200


if __name__ == '__main__':
    host = os.environ.get('STUB_HOST', '127.0.0.1')
    port = os.environ.get('STUB_PORT', '4444')

    app.run(host, port)
