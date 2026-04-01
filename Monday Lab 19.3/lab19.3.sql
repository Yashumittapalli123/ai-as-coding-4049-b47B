#Task 01
import sqlite3

conn = sqlite3.connect("university.db")
cur = conn.cursor()

# Tables
cur.execute("CREATE TABLE IF NOT EXISTS Students(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Faculty(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Courses(id INTEGER PRIMARY KEY, name TEXT, faculty_id INTEGER)")
cur.execute("""CREATE TABLE IF NOT EXISTS Registrations(
id INTEGER PRIMARY KEY,
student_id INTEGER,
course_id INTEGER)""")

# Queries
print("Students in Course:")
for row in cur.execute("""
SELECT s.name
FROM Students s
JOIN Registrations r ON s.id = r.student_id
WHERE r.course_id = 1
"""):
    print(row)

print("\nFaculty teaching >2 courses:")
for row in cur.execute("""
SELECT f.name, COUNT(c.id)
FROM Faculty f
JOIN Courses c ON f.id = c.faculty_id
GROUP BY f.id
HAVING COUNT(c.id) > 2
"""):
    print(row)

print("\nMost Registered Course:")
for row in cur.execute("""
SELECT c.name, COUNT(r.student_id) as total
FROM Courses c
JOIN Registrations r ON c.id = r.course_id
GROUP BY c.id
ORDER BY total DESC
LIMIT 1
"""):
    print(row)

conn.close()

#Task 02 :
# SQL Queries for E-commerce Database

# Query 1: Retrieve all orders for user_id = 1
query1 = """
SELECT o.id, o.user_id, o.date
FROM Orders o
WHERE o.user_id = 1
ORDER BY o.date DESC;
"""

# Query 2: Find most purchased product (based on total quantity)
query2 = """
SELECT p.id, p.name, SUM(od.quantity) as total_quantity
FROM Products p
JOIN OrderDetails od ON p.id = od.product_id
GROUP BY p.id, p.name
ORDER BY total_quantity DESC
LIMIT 1;
"""

# Query 3: Calculate total revenue for March month
query3 = """
SELECT SUM(p.price * od.quantity) as total_revenue
FROM OrderDetails od
JOIN Products p ON od.product_id = p.id
JOIN Orders o ON od.order_id = o.id
WHERE MONTH(o.date) = 3 AND YEAR(o.date) = YEAR(GETDATE());
"""

print("Query 1:", query1)
print("Query 2:", query2)
print("Query 3:", query3)

#Task 03 :
# SQL Queries for E-commerce Database

# Query 1: Retrieve all orders for user_id = 1
query1 = """
SELECT o.id, o.user_id, o.date
FROM Orders o
WHERE o.user_id = 1
ORDER BY o.date DESC;
"""

# Query 2: Find most purchased product (based on total quantity)
query2 = """
SELECT p.id, p.name, SUM(od.quantity) as total_quantity
FROM Products p
JOIN OrderDetails od ON p.id = od.product_id
GROUP BY p.id, p.name
ORDER BY total_quantity DESC
LIMIT 1;
"""

# Query 3: Calculate total revenue for March month
query3 = """
SELECT SUM(p.price * od.quantity) as total_revenue
FROM OrderDetails od
JOIN Products p ON od.product_id = p.id
JOIN Orders o ON od.order_id = o.id
WHERE MONTH(o.date) = 3 AND YEAR(o.date) = YEAR(GETDATE());
"""

print("Query 1:", query1)
print("Query 2:", query2)
print("Query 3:", query3)

#task04 :
import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Tables
cur.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY, title TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Members(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("""CREATE TABLE IF NOT EXISTS Loans(
id INTEGER PRIMARY KEY,
book_id INTEGER,
member_id INTEGER,
loan_date TEXT,
return_date TEXT)""")

# Queries
print("Issued Books:")
for row in cur.execute("""
SELECT b.title, m.name
FROM Loans l
JOIN Books b ON l.book_id = b.id
JOIN Members m ON l.member_id = m.id
WHERE l.return_date IS NULL
"""):
    print(row)

print("\nOverdue Books:")
for row in cur.execute("""
SELECT b.title, m.name
FROM Loans l
JOIN Books b ON l.book_id = b.id
JOIN Members m ON l.member_id = m.id
WHERE julianday('now') - julianday(l.loan_date) > 30
"""):
    print(row)

print("\nBooks per Member:")
for row in cur.execute("""
SELECT m.name, COUNT(l.book_id)
FROM Members m
LEFT JOIN Loans l ON m.id = l.member_id
GROUP BY m.id
"""):
    print(row)

conn.close()

#Task 05 :
import sqlite3

conn = sqlite3.connect("university.db")
cur = conn.cursor()

# Tables
cur.execute("CREATE TABLE IF NOT EXISTS Students(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Faculty(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Courses(id INTEGER PRIMARY KEY, name TEXT, faculty_id INTEGER)")
cur.execute("""CREATE TABLE IF NOT EXISTS Registrations(
id INTEGER PRIMARY KEY,
student_id INTEGER,
course_id INTEGER)""")

# Queries
print("Students in Course:")
for row in cur.execute("""
SELECT s.name
FROM Students s
JOIN Registrations r ON s.id = r.student_id
WHERE r.course_id = 1
"""):
    print(row)

print("\nFaculty teaching >2 courses:")
for row in cur.execute("""
SELECT f.name, COUNT(c.id)
FROM Faculty f
JOIN Courses c ON f.id = c.faculty_id
GROUP BY f.id
HAVING COUNT(c.id) > 2
"""):
    print(row)

print("\nMost Registered Course:")
for row in cur.execute("""
SELECT c.name, COUNT(r.student_id) as total
FROM Courses c
JOIN Registrations r ON c.id = r.course_id
GROUP BY c.id
ORDER BY total DESC
LIMIT 1
"""):
    print(row)

conn.close()
