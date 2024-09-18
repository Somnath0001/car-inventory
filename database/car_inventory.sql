-- car_inventory.sql

CREATE DATABASE car_inventory;

USE car_inventory;

CREATE TABLE cars (
  id INT AUTO_INCREMENT,
  company VARCHAR(255),
  name VARCHAR(255),
  make VARCHAR(255),
  model VARCHAR(255),
  PRIMARY KEY (id)
);