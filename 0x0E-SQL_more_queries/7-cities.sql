-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
