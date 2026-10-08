## Except try, Except block
try:
    a = b
except:
    print("The variable is not assigned yet")

try:
    a = b
except NameError as ex:
    print(ex)