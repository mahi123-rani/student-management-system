CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    gender VARCHAR(10),
    dob VARCHAR(20),
    stream VARCHAR(50)
);
