
# lst = []
# for x in range(10):
#     lst.append(x**2)


# print(lst)
lst = [x**2 for x in range(10)]
# print(lst)

even_numbers = [z for z in range(10) if (z%2 == 0) ]
# print(even_numbers)

# nested list comprehension
lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b' , 'c', 'd']
pair = [[i,j] for i in lst1 for j in lst2]
# print(pair)

# List comprehension using function calls
names = ["Arpit", "Shristy", "Abhishek", "Sakshi"]
lengths = [ len(name) for name in names]
print(lengths)