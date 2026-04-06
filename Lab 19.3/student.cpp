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
