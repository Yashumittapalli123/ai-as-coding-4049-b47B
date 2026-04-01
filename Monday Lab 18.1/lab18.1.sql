--Database Design and Queries: Schema Design and SQL Generation
--Task-1: Hospital Management System
--Create a table with the information of Doctors, Patients, Appointments. With their Unique ID's, valid dates using Joins.
DROP TABLE IF EXISTS Doctors;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Appointments;

CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(50),
    specialization VARCHAR(50),
    contact_number VARCHAR(15)
);
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    contact_number VARCHAR(15)
);
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    appointment_date DATE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
--Insert some data into the tables
INSERT OR IGNORE INTO Doctors (doctor_id, name, specialization, contact_number) VALUES (1, 'Dr. Smith', 'Cardiology', '1234567890'),
(2, 'Dr. Johnson', 'Neurology', '0987654321'),
(3, 'Dr. Williams', 'Pediatrics', '5556667777'),
(4, 'Dr. Brown', 'Orthopedics', '4445556666'),
(5, 'Dr. Jones', 'Dermatology', '3334445555');

INSERT OR IGNORE INTO Patients (patient_id, name, age, contact_number) VALUES (1, 'Alice', 30, '1112223333'),
(2, 'Bob', 25, '4445556666'),
(3, 'Charlie', 35, '7778889999'),
(4, 'David', 40, '3334445555'),
(5, 'Eve', 28, '2223334444');
INSERT OR IGNORE INTO Appointments (appointment_id, doctor_id, patient_id, appointment_date) VALUES (1, 1, 1, '2023-10-01'),
(2, 2, 2, '2023-10-02'),
(3, 3, 3, '2023-10-03'),
(4, 4, 4, '2023-10-04'),
(5, 5, 5, '2023-10-05');
--List all appointments for a specific Doctor
SELECT a.appointment_id, d.name AS doctor_name, p.name AS patient_name, a.appointment_date
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
JOIN Patients p ON a.patient_id = p.patient_id
WHERE d.doctor_id = 1;  -- Replace 1 with the desired doctor's ID
--Retrieve patient history by patient ID.
SELECT a.appointment_id, d.name AS doctor_name, a.appointment_date
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1;  -- Replace 1 with the desired patient's ID
--Count total patients treated by each doctor.
SELECT d.name AS doctor_name, COUNT(a.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.name;

--Task-2: Real-Time Application: Online Shopping Database
--Design a database for an E-commerce platform with Tables: Users, Products, Orders, OrderDetails.
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderDetails;
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    contact_number VARCHAR(15)
);
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10, 2),
    stock INT
);
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE OrderDetails (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
--Retrieve all orders by a user.
SELECT o.order_id, o.order_date, p.name AS product_name, od.quantity
FROM Orders o JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE o.user_id = 1;  -- Replace 1 with the desired user's ID
--Find the most purchased product.
SELECT p.name AS product_name, SUM(od.quantity) AS total_quantity
FROM Products p JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.name
ORDER BY total_quantity DESC
LIMIT 1;
--Calculate total revenue in a given month.
SELECT SUM(p.price * od.quantity) AS total_revenue
FROM Orders o JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE strftime('%Y-%m', o.order_date) = '2023-10';  -- Replace '2023-10' with the desired month and year

--Additional optimization: Ensure indexes exist for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_orders_user_id ON Orders(user_id);
CREATE INDEX IF NOT EXISTS idx_orderdetails_product_id ON OrderDetails(product_id);
CREATE INDEX IF NOT EXISTS idx_orderdetails_order_id ON OrderDetails(order_id);

--Task-3: Library Management System
--Schema Design
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Loans;

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    publication_year INT,
    genre VARCHAR(50)
);

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    membership_date DATE
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

--Indexing Strategy
--1. Create an index on the `loan_date` column in the `Loans` table for faster retrieval of overdue books.
CREATE INDEX idx_loan_date ON Loans(loan_date);
--2. Create an index on the `member_id` column in the `Loans` table for faster aggregation of books loaned by each member.
CREATE INDEX idx_member_id ON Loans(member_id);
--3. Create an index on the `book_id` column in the `Loans` table for faster retrieval of issued books.
CREATE INDEX idx_book_id ON Loans(book_id);

--Insert sample data
INSERT INTO Books (book_id, title, author, publication_year, genre) VALUES
(1, '1984', 'George Orwell', 1949, 'Dystopian'),
(2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

INSERT INTO Members (member_id, name, membership_date) VALUES
(1, 'Alice', '2023-01-15'),
(2, 'Bob', '2022-06-20'),
(3, 'Charlie', '2021-03-10');

INSERT INTO Loans (loan_id, book_id, member_id, loan_date, return_date) VALUES
(1, 1, 1, '2026-03-01', NULL),
(2, 2, 2, '2026-02-15', '2026-03-10'),
(3, 3, 3, '2026-01-20', NULL);

--SQL Queries demonstrating joins and conditions
--1. Retrieve all books currently issued
SELECT b.book_id, b.title, m.name AS member_name, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;

--2. Find overdue books (loan date > 30 days)
SELECT b.book_id, b.title, m.name AS member_name, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL AND l.loan_date < DATE('now', '-30 days');

--3. Count number of books loaned by each member
SELECT m.member_id, m.name AS member_name, COUNT(l.loan_id) AS books_loaned
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.name;


--Task-4: Optimized Queries
--Original query: Retrieve all orders by a user
--Optimized query: Use indexes and joins for efficiency
SELECT o.order_id, o.order_date, p.name AS product_name, od.quantity
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE o.user_id = 1;  -- Replace 1 with the desired user's ID

--Original query: Find the most purchased product
--Optimized query: Use aggregation and indexing
SELECT p.name AS product_name, SUM(od.quantity) AS total_quantity
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.name
ORDER BY total_quantity DESC
LIMIT 1;

--Original query: Calculate total revenue in a given month
--Optimized query: Use date functions and indexing
SELECT SUM(p.price * od.quantity) AS total_revenue
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE strftime('%Y-%m', o.order_date) = '2023-10';  -- Replace '2023-10' with the desired month and year


--Task-5: University Course Registration
--Schema Design
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Registrations;

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    enrollment_date DATE
);

CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    name VARCHAR(100),
    faculty_id INT,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
);

CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    registration_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

--Insert sample data
INSERT INTO Students (student_id, name, enrollment_date) VALUES
(1, 'Alice', '2023-01-15'),
(2, 'Bob', '2022-06-20'),
(3, 'Charlie', '2021-03-10');

INSERT INTO Faculty (faculty_id, name, department) VALUES
(1, 'Dr. Smith', 'Computer Science'),
(2, 'Dr. Johnson', 'Mathematics'),
(3, 'Dr. Williams', 'Physics');

INSERT INTO Courses (course_id, name, faculty_id) VALUES
(1, 'Data Structures', 1),
(2, 'Algorithms', 1),
(3, 'Linear Algebra', 2),
(4, 'Quantum Mechanics', 3);

INSERT INTO Registrations (registration_id, student_id, course_id, registration_date) VALUES
(1, 1, 1, '2026-03-01'),
(2, 2, 1, '2026-03-02'),
(3, 3, 2, '2026-03-03'),
(4, 1, 3, '2026-03-04'),
(5, 2, 4, '2026-03-05');

--SQL Queries
--1. List all students enrolled in a specific course
SELECT s.student_id, s.name AS student_name, c.name AS course_name
FROM Registrations r
JOIN Students s ON r.student_id = s.student_id
JOIN Courses c ON r.course_id = c.course_id
WHERE c.course_id = 1;  -- Replace 1 with the desired course ID

--2. Find faculty members teaching more than 2 courses
SELECT f.faculty_id, f.name AS faculty_name, COUNT(c.course_id) AS courses_taught
FROM Faculty f
JOIN Courses c ON f.faculty_id = c.faculty_id
GROUP BY f.faculty_id, f.name
HAVING COUNT(c.course_id) > 2;

--3. Retrieve courses with the highest number of registrations
SELECT c.course_id, c.name AS course_name, COUNT(r.registration_id) AS total_registrations
FROM Courses c
JOIN Registrations r ON c.course_id = r.course_id
GROUP BY c.course_id, c.name
ORDER BY total_registrations DESC
LIMIT 1;
