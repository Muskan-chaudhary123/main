# function to check the given number is odd or even

"""def is_even(num):"""

"""this function return the given number is odd or even
input - any valid number
output - odd/even"""

"""if type(num) == int:
        if num%2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'wrong data type,pls enter int '

for i in range(1,11):
    x = is_even(i)
    print(x)"""

# default argument
"""def multiply(*args):
    product = 1
    for i in args:
        product = product*i
    print(args)
    return product


print(multiply(2,4,7,8,2,1))
"""

"""def capitals(**kwargs):
    for (key, value) in kwargs.items():
        print(key, '-', value)
    return (key,value)


print(capitals(india='delhi', srilanka='colombo', nepal='kathmandu'))"""

"""def f(y):
    x = 1
    x += 1
    print(x)


x = 5
f(x)

print(x)"""

"""def f(x):
    x = x + 1
    print('in f(x):', x)
    return x


x = 3
z = f(x)
print('in main program scope:z = ',z)
print('in main program scope:x = ',x)"""

"""def g(x):
    def h():
            x = 'abc'
    x = x + 1
    print('in g(x) : x = ',x)
    h()
    return x

x = 3
z = g(x)"""

"""def g(x):
    def h(x):
        x = x +1
        print('x in h(x): x =',x)
    x = x+1
    print('x in g(x): x =', x)
    h(x)
    return x


x = 3
z = g(x)
print('in main program scope : x = ',x)
print('in main program scope : z = ',z)"""

"""def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4)
print(val)"""

# function as argument can be passed
"""def fun_a():
    print('inside fun_a')


def fun_b(z):
    print('inside fun_c')
    return z()


fun_b(fun_a)"""

"""def square(x):
    return x**2


def transform(f,l):
    output = []
    for i in l:
        output.append(f(i))

    print(output)


l = [1,2,3,4,5]
transform(square,l)"""

# fetching names from a list of dictionary

"""user = [
    {
        'name': 'Nitish',
        'age': 33,
        'gender': 'male',
        'grade': 'skilled'

    },
    {
        'name': 'ankita',
        'age': 50,
        'gender': 'male',
        

    },
    {
        'name': 'rahul',
        'age': 45,
        'gender': 'male'
    }
]

print(list(filter(lambda user:user['name'],user )))"""

















