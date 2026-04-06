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
