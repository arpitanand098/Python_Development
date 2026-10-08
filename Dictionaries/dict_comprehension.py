squares = {x : x**2 for x in range(5)}
print(squares)

# Conditional dictionary comprehension
even_squares = {z: z**2 for z in range(10) if (z%2 == 0) }
print(even_squares)