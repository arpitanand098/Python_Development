student = {
    "name": "Arpit",
    "age": 32,
    "grade": 6.95
}
#Iterating over keys
for keys in student.keys():
    print(keys)

#Iterate over values
for values in student.values():
    print(values)

#iterate over the key value pairs
for key,value in student.items():
    print(f"{key}:{value}")