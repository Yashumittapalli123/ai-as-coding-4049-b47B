Task 1 – Python to C++ Conversion

Task:
Translate a simple Python class into C++ using AI assistance.

Instructions:
• Prompt AI to convert a Python class representing a Student with attributes and methods into equivalent C++ code
• Ensure proper handling of:
  o Constructors
  o Data types
  o Access specifiers
• Compile and run both versions to verify output consistency

Expected Output:
An equivalent working C++ class translated from Python.

Python Code (student.py):
```python
# Python Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Example usage
if __name__ == "__main__":
    student = Student("Alice", 20, 'A')
    student.display()
```

C++ Code (student.cpp):
```cpp
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;
    char grade;

public:
    // Constructor
    Student(std::string n, int a, char g) : name(n), age(a), grade(g) {}

    // Method to display student info
    void display() {
        std::cout << "Name: " << name << ", Age: " << age << ", Grade: " << grade << std::endl;
    }
};

int main() {
    Student student("Alice", 20, 'A');
    student.display();
    return 0;
}
```

Verification:
Python output: Name: Alice, Age: 20, Grade: A
C++ output (expected): Name: Alice, Age: 20, Grade: A

Note: C++ compilation requires a C++ compiler like g++ or cl.exe. On this system, g++ is not available, so compilation was not performed, but the code is syntactically correct and should produce the same output when compiled and run.
