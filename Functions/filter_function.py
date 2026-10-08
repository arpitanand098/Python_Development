
def even(num):
    if num%2 == 0:
        return True
    
    
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(even,lst)))

odd = list(filter(lambda x:x%2 !=0, lst))
print(odd)

##Filter with Lambda Function with multiple condition
odd_greater_than_five = list(filter(lambda x:x%2 !=0 and x>5, lst))
print(odd_greater_than_five)

#filter() to check if the age is greater than 18 in dictionaries
people =[
    {'name':"Arpit", 'age': 20},
    {'name':"Abhi", 'age': 21},
    {'name':"Ankit", 'age': 17}
]

def age(people):
    return people['age'] > 18

print(list(filter(age,people)))