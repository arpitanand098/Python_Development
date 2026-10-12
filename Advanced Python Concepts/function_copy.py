def welcome():
    return 'Welcome to the advanced python course'

print(welcome())

wel = welcome
print(wel())
del welcome
print(wel())
# print(welcome())

