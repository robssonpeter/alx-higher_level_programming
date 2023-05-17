-- Create db and user
-- Creates a database hbtn and user user_od_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'locahost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT FOR hbtn_0d_2.* TO 'user_0d_2';
