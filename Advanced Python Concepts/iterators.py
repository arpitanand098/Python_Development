my_list = [1, 2, 3, 4, 5, 6]
for i in my_list:
    print(i)

print(type(my_list))
print(my_list)

### Iterator
iterator = iter(my_list)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")

# print(type(iterator))
# print(iterator)

## Iterate Through All The Element

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
