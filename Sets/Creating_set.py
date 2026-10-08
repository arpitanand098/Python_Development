my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))

set = set([1, 2, 3, 4, 7, 4, 5, 6, 7])
# print(set)

#adding an element
set.add(8)
# print(set)

#removing the element
set.remove(3)
# print(set)
set.discard(10)

##pop method 
removed_element = set.pop()
print(removed_element)
print(set)

my_set.clear()
print(my_set)