-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the data base
USE hbtn_0d_usa;
-- CREATE TABLE INSIDE DATABASE AND CHECK IF NOT EXISTS CREATE IT
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT  PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);