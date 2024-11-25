# sum of n natural no
# 1. using recursion
"""def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))"""

# 2. using for loop:
"""n = int(input("enter num here : "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)"""

# 3. using function:
"""def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

print(sum(5))"""

# to count number of digit

"""n = int(input("enter num here : "))
i = 0
while n > 0:
    n = n//10
    i = i+1
    
print(+i)"""
# palindrome no
# using string
"""n = input("enter num : ")
rev = n[::-1]
if n == rev:
    print("given no is palindrome")
else:
    print("not palindrome")"""

# using reversing the digit

"""n = int(input("enter num here : "))
rev = 0
temp = n
while temp != 0:
    ld= temp% 10
    rev = rev*10 + ld
    temp = temp//10

if n == rev:
    print("palindrome")
else:
    print("not palindrome")"""

# factorial of number:
# 1. using loop:
"""n = int(input("enter num :"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)"""

# using recursion:
"""def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))"""

# GCD of two number:
"""a = int(input("enter value of a : "))
b = int(input("enter value of b : "))

if a > b:
    smaller = b
else:
    smaller = a
for i in range(1, smaller+1):
    if a % i == 0 and b % i == 0:
        hcf = i
print("hcf is : ", hcf)"""

# LCM
"""a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
if a > b:
    greater = a
else:
    greater = b
value = greater
while True:
    if greater%a == 0 and greater%b == 0:
        print("lcm is :", greater)
        break
    else:
        greater = greater + value"""

# check prime:
"""n = int(input("enter num here : "))
if n > 1:
    for i in range(2,n):
        if n%i == 0:
            print("given number is not prime number ")
            break
    else:
        print(n, " is a prime number")"""

# prime factorisation:
"""x = int(input("enter num here:"))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True


def prime_factor(x):
    for i in range(2, x + 1):
        if is_prime(i):
            n = i
            while x % n == 0:
                print(i)
                n = n*i


print(prime_factor(100))"""

# to print all divisors of  a number in increasing order
"""n = int(input("enter num here : "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)"""

# sieve of  eratosthenes:


"""def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
            break
    return True


def sieve_ert(n):
    for i in range(2, n):
        if is_prime(i):
            print(i)


print(sieve_ert(10))"""

# compute power:

"""def power(x,n):
    res = 1
    for i in range(n):
        res = res*x
    return res

print(power(2,4))"""


"""class Solution:
    def __init__(self,n):
        self.n = n
        self.fact = 1

    def factorial(self):
        
        for i in range(1, self.n + 1):
            self.fact = self.fact*i
        return self.fact


obj = Solution(5)
print(obj.factorial())"""

print(99996%39)







