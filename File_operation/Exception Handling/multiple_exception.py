try:
    num = int(input("Enter a Number: "))
    result = 12/ num
except ValueError as e:
    print("Please Enter a valid number")
except ZeroDivisionError as e1:
    print("Error:", e1)
    print("Please enter number other than zero")
except Exception as ex2:
    print("Error:", ex2)