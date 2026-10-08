# map():- Applies a function to all items in a list
numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x*x, numbers)))

##can we map multiple iterables
numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers = list(map(lambda x,y:x + y, numbers1,numbers2))
print(added_numbers)

##map() to convert a list of strings to integers
str_numbers = ['1', '2', '3', '4','5', '6']
int_numbers = list(map(int, str_numbers))

print(int_numbers)


##map() dict 
def get_name(person):
    return person['name']

people =[
    {'name':"Arpit", 'age': 20},
    {'name':"Abhi", 'age': 21},
    {'name':"Ankit", 'age': 17}
]
print(list(map(get_name, people)))