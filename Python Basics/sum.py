number = int(input("Enter a Number: "))
sum = 0
count = 1

while(count <= number):
    sum = sum + count
    count = count + 1
    print("Sum of first " + number + " natural number is: ", sum)
