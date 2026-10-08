mixed_tuple = (42, "Arpit", 6.95, False)
print(mixed_tuple.count(1))
print(mixed_tuple.index(6.95))

# Packing and unpacking Tuple
packed_tuple=1, "Arpit", 6.95
print(packed_tuple)

##Unpacking
a,b,c = packed_tuple

print(a)
print(b)
print(c)

# Unpackin with *
numbers = tuple([1, 2, 3, 4, 5, 6])
first, *middle, last = numbers
print(first)
print(middle)
print(last)