-- create database if not exits 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa
USE hbtn_0d_usa;
-- CREATE TABLE CITIES
CREATE TABLE IF NOT EXISTS cities(
    id INT  AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES state(id),
    name VARCHAR(256) NOT NULL,
);
