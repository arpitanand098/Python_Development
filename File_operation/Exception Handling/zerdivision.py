try:
    result = 1/0
except ZeroDivisionError as e:
    print("Error:", e)

try:
    result = 1/2
    a = b
except ZeroDivisionError as e:
    print("Error:", e)
    print("Please enter the denominator other than zero")
except Exception as ex1:
    print("Error:", ex1)
    print("Main exception got caught here")