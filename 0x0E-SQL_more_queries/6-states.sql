-- Create table hbtn_0d_usa
-- Creates the table and add state
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE TABLE states IF NOT EXISTS (id INT UNIQUE, name VARCHAR(256) NOT NULL);
