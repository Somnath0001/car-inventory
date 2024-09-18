# backend/app.py

from flask import Flask, request, jsonify, render_template, send_from_directory
from database import get_cars, add_car, search_car
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frontend/<path:path>')
def send_frontend(path):
    return send_from_directory('../frontend', path)

@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars = get_cars()
    return jsonify([{'id': car[0], 'company': car[1], 'name': car[2], 'make': car[3], 'model': car[4]} for car in cars])

@app.route('/cars', methods=['POST'])
def create_car():
    car_data = request.json
    add_car(car_data)
    return jsonify({'message': 'Car added successfully'}), 201

@app.route('/cars/search', methods=['GET'])
def search_car_by_name():
    name = request.args.get('name')
    cars = search_car(name)
    return jsonify([{'id': car[0], 'company': car[1], 'name': car[2], 'make': car[3], 'model': car[4]} for car in cars])

if __name__ == '__main__':
    app.run(debug=True)