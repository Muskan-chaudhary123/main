# recursive function
# factorial through loop:
"""n = int(input("enter num here: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)"""


# factorial through recursion

"""def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))"""

# sum of n natural no through loop:
"""n = int(input("enter num here : "))
sum = 0
for i in range(0, n+1):
    sum = sum + i
print(sum)"""

# sum of n natural number using recursion:


"""def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)


print(sum(3))"""


# to print all elements of a list using loop:
"""l = [1, 2, 3, 4, 5, 6]
for i in l:
    print(i)"""

# to print all elements of a list using recursion:


"""def print_list(list, idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list,idx+1)

l = [1,2,3,4,5,6,7]
print(print_list(l,0))"""


"""def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")

    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))"""


arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
res = []
for i in range(1,n):
    if arr[i-1] < arr[i]:
        res.append(arr[i])
res.append(arr[n-1])

print(res)















