num = int(input("Enter a Number: "))
if num > 0: 
    print("The number is positive")
    if num % 2 == 0:
        print("the number is even")
    else:
        print("The number is odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")