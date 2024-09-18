# backend/database.py

import mysql.connector
from config import DB_CONFIG

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

def get_cars():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM cars"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

def add_car(car_data):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO cars (company, name, make, model) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, tuple(car_data.values()))
    db.commit()
    db.close()

def search_car(name):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM cars WHERE name LIKE %s"
    cursor.execute(query, (f"%{name}%",))
    results = cursor.fetchall()
    db.close()
    return results