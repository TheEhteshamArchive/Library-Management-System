#Why the hell cant I make a databse LIBRARY :/
CREATE DATABASE IF NOT EXISTS Management;
USE Management;

create table if not exists books(
    book_id int AUTO_INCREMENT PRIMARY KEY,
    title VarChar(100) NOT NULL,
    author VarChar(100) NOT NULL,
    quantity int NOT NULL
);

create table if not exists students(
    student_id int AUTO_INCREMENT PRIMARY KEY,
    name VarChar(100) NOT NULL
);

create table if not exists issued_books(
    issue_id int AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    book_id int,
    issue_date date,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);