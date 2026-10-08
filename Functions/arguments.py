## Positional Arguments
def print_numbers(*args):
    for number in args:
        print(number)

# print_numbers(1,2,3,4,5,6,6,7,"Arpit") 

def print_info(**kwargs):
    for key,value in kwargs.items():
            print(f"{key}:{value}")

print( Name="Arpit", Age = "20", City= "Patna")


## keywords Arguments
def print_details(*args,**kwargs):
      for val in args:
            print(f"Postional Argument: {val}")
    
      for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(1, 2, 3, 4, 5, Name="Arpit", Age = "20", City= "Patna") # Positional arguments always comes befor the Keyword Argument.