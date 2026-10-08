names = ["Arpit", "Shristy", "Abhishek", "Sakshi"]
names.append("Rishita")
# print(name)

names.insert(3, "Babli")
# print(name)

# remove and return the last element
popped_name = names.pop()
# print(popped_name)

index = names.index("Shristy")
# print(index)

names.sort()
# print(name)

names.reverse()
# print(name)

# Iterating Over the List
for name in names:
    print(name)
    
for index, name in enumerate(names):
    print(index, name)