## Nested List
lst=[[1,2,3,4],[42,"Arpit",6.95],[2,"yut",50]]
print(lst[1][1])

lst=[[1,2,3,4],[42,"Arpit",6.95],(2,"yut",50)]
print(lst[2][0:2])

##Nested Tuples
nested_tuples = ((1, 2, 3), ("a","b","c"),(True, False))
print(nested_tuples[0])
print(nested_tuples[1][2])

##Iterating Over nested Tuples
for sub_tuple in nested_tuples:
    for item in sub_tuple:
        print(item, end=" ")
    print()
