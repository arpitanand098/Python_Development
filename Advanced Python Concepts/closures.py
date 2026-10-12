''' +++++++ Closures Functions ++++++++++'''

# def main_welcome(msg):
    
#     def sub_welcome_method():
#         print("Welcome to the advanced python course")
#         print(msg)
#         print("Please Learn these concepts properly")

#     return sub_welcome_method()

# main_welcome("Welcome Everyone")


def main_welcome(func):
    
    def sub_welcome_method():
        print("Welcome to the advanced python course")
        (func("Welcome everyone to this tutorial"))
        print("Please Learn these concepts properly")

    return sub_welcome_method()

main_welcome(print)