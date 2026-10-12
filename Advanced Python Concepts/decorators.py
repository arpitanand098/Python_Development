
def main_welcome(func):
    
    def sub_welcome_method():
        print("Welcome to the advanced python course")
        func()
        print("Please Learn these concepts properly")

    return sub_welcome_method()

# def course_introduction():
#     print("This is an advanced python course")

# main_welcome(course_introduction)

@main_welcome
def course_introduction():
    print("This is an advanced python course")


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()

### Decorators with arguments
def repeat(n):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return func_wrapper
    return decorator


@repeat(3)
def greet():
    print("Namaste!")

greet()