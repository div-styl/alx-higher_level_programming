-- create database if not exits 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa
USE hbtn_0d_usa;
-- CREATE TABLE CITIES
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES state(id),
);
