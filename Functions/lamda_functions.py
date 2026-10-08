## Syntax 
# lambda arguments: expression

addition = lambda a,b: a + b
print(type(addition))
print(addition(5,6))

even = lambda num: num%2 == 0
print(even(25))

sum = lambda x,y,z : x + y + z
print(sum(36, 38, 42))