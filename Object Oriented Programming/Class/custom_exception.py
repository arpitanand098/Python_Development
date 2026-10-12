class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter your Date Of Birth"))
age = 2026 -year

try:
    if age <= 30 and age>= 20:
        print("You are Eligible for the Exam")
    else:
        raise dobException

except dobException:
    print("Sorry, your age should be greater than 20 or less than 30")