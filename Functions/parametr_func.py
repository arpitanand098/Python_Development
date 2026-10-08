def sum(a,b):
    # add = a + b
    # print("The sum is", add)
    return a + b

print(sum(5,6))


##Default Parameter
def greet(name = "Guest"):
    print(f"Hello {name} Welcome to the Jungle")

greet()
greet("Arpit")