student = {
    "name": "Arpit",
    "age": 32,
    "grade": 6.95
}
student_copy = student
print(student)
print(student_copy)

student["name"] = "Abhishek"
print(student)
print(student_copy)

##Shallow Copy
student_copy1 = student.copy()
print(student_copy1)
print(student)

student["name"] = "Arpit"
print(student_copy1)
print(student)