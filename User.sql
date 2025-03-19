-- Create Database
CREATE DATABASE todolist;

-- Use the Database
USE todolist;

-- Create Table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL
);
select * FROM tasks;
