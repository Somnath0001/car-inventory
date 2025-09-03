from flask import Flask, request, jsonify, render_template, send_from_directory
from database import get_cars, add_car, search_car
import os
from flasgger import Swagger, swag_from

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app.config["SWAGGER"] = {"title": "Car Inventory API"}
swagger = Swagger(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/frontend/<path:path>')
def send_frontend(path):
    return send_from_directory('../frontend', path)


@app.route('/cars', methods=['GET'])
@swag_from("cars.yml")
def get_all_cars():
    try:
        cars = get_cars()
        return jsonify([{'id': car[0], 'company': car[1], 'name': car[2], 'make': car[3], 'model': car[4]} for car in cars])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/cars', methods=['POST'])
@swag_from("create_car.yml")
def create_car():
    try:
        car_data = request.json
        add_car(car_data)
        return jsonify({'message': 'Car added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/cars/search', methods=['GET'])
@swag_from("search_cars.yml")
def search_car_by_name():
    try:
        name = request.args.get('name')
        cars = search_car(name)
        return jsonify([{'id': car[0], 'company': car[1], 'name': car[2], 'make': car[3], 'model': car[4]} for car in cars])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)