students = {
    "student1" : {"name": "Arpit", "Reg_no": 42},
    "student2" : {"name": "Abhishek", "Reg_no": 36},
    "student3" : {"name": "Shristy", "Reg_no": 38},
}
print(students)

#Access nested Dictionaries elements
print(students["student1"]["name"])
print(students["student3"]["name"])

##Iterating Over nested Dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")
