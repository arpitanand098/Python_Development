set = {1, 2, 3, 4, 5}
print(3 in set)
print(7 in set)

##Mathematical operation
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(union_set)

Intersection_set = set1.intersection(set2)
print(Intersection_set)

# set1.intersection_update(set2)
# print(set1)

#Difference
print(set2.difference(set1))

#Syemmetric Difference
print(set1.symmetric_difference(set2))