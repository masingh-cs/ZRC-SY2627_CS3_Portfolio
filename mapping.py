class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name):
        self.name = name



course = Course("Math 3")


student1 = Student("Mauris")
student2 = Student("John")


course.add_student(student1)
course.add_student(student2)


print("Course:", course.name)
print("Students in the course:")

for student in course.students:
    print("-", student.name)
