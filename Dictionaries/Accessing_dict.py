student = {
    "name": "Arpit",
    "age": 20,
    "grade": 6.95
}

print(student['grade'])
print(student.get('age'))
print(student.get('last_name'))
print(student.get('last_name', "Not Available"))