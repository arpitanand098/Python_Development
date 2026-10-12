def square(n):
    for i in range(3):
        # return i**2
        yield i**2
     

print(square(3))

for i in square(3):
    print(i)

a = square(3)
print(next(a))
print(next(a))
print(next(a))

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

## Practical : Reading Large Files
'''Generators are a particularly useful for reading Large files because they allow you to process one line at a time without loading the entire file into memory.'''

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

file_path = 'large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())

