"""def outer():
    a = 1
    def inner():
        nonlocal a
        a += 1
        print(a)
    inner()
    print(a)

outer()
print("main program")"""
import time

# in python functions are first class citizens :
# in this code we are giving 1 function square2 as input to square1 function this is same behaviour that decorator show


"""def square1(fun, num):
    return fun(num)


def square2(num):
    return num**2


print(square1(square2, 2))"""

"""def my_decorator(func):
    def wrapper():
        print("*******************")
        func()
        print("*******************")
    return wrapper()

@my_decorator
def hello():
    print("hello")


hello()"""

# decorator to print the time execution of any function


"""import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("time taken by", func.__name__, time.time() - start, "sec")

    return wrapper


@timer
def hello():
    print("hello world")
    time.sleep(2)


@timer
def square(num):
    time.sleep(1)
    print(num**2)


hello()
square(5)"""

# function to check the given data of variable is correct or not
# so here decorator will expect an input except function
# here two wrappers are required one inner wrapper and one outer wrapper:


def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("this data type is not allowed")
        return inner_wrapper
    return outer_wrapper


@sanity_check(int)
def square(num):
    print(num**2)

square(4)


@sanity_check(str)
def greet(name):
    print("hello",name)









