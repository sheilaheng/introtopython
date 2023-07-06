from database import User

users = User.select()
# Use forloop to display
for user in users:
    print(user.name, user.email, user.password)

from database import Student
students = Student.select()
# Use forloop to display
for student in students:
    print(student.name, student.phone, student.age, student.gender, student.studentcode)
