list = [2, 3, 4, 3, 6, 5, 4, 7, 8, 3, 6, 7, 8, 9, 5, 4, 8, 9, 4, 6, 7, 8, 9, 0, 6, 3, 5]
frequency = {}

for number in list:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] =1
print(frequency)