-- Create table hbtn_0d_usa
-- Creates the table and add state
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE TABLE cities IF NOT EXISTS (id INT UNIQUE, state_id INT, name VARCHAR(256) NOT NULL) FOREIGN KEY (state_id) REFERENCES states(id);
