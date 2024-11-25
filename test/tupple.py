# swapping of two numbers
"""a =1
b = 2
c = a
a = b
b = c
print(a)
print(b)"""
# 2 nd method
"""a =1
b = 2
a,b = b,a
print(a)
print(b)"""

"""t1 = tuple(input("enter the first tuple : "))
t2 = tuple(input("enter the first tuple : "))
if t1 == t2:
    print("same tuple")
else:
    print("not same")"""

"""t = (1,5,7,8,10)
print(tuple([i*j for i,j in zip(t,t[1:])]))"""

"""list = [{'hi','bye'},{'geeks','for geeks'},('a','b'),['hi','bye'],['a','b']]
for i in list:
    
    print(i)"""

"""l1 = [1,5,10,20,40,80]
l2 = [6,7,20,80,100]
l3 = [3,4,15,20,30,70,80,120]
x = set(l1).intersection(set(l2))
print(list(x.intersection(set(l3))))"""

"""l1 = [1,5,10,20,40,80]
l2 = [6,7,20,80,100]
l3 = [3,4,15,20,30,70,80,120]
l4 = []
[l4.append(i) for i in l1 if i in l2 and i in l3]
print(list(set(l4)))"""

"""days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
temp_c = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
# method 1:
print(dict(zip(days,temp_c)))
# method 2:
print({i:j for (i,j) in zip(days,temp_c)})"""

"""products = {'phone': 10 ,'laptop': 0,'charger': 32 ,'tablet':0}


print({i: products[i] for i in products if products[i]!=0})"""

# nested comprehension

"""print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})"""

























