"""n = int(input("enter num here : "))
sum = 0
for i in range(1, n+1):
    if i % 5 == 0:
        continue
    sum = sum + i
    if sum +i > 300:
        break

print(sum)"""

"""num = 1
sum = 0
avg = 0
i = 0
while num != 0:
    num = int(input("enter num here : "))
    sum = sum+num
    i = i + 1
if i == 0:
    print("enter sum input")
else:
    avg = sum / (i - 1)

print(sum)
print(avg)
print(i)"""

# reverse list
"""l = [1,6,4,89,54,32,12]
s = 0
e = len(l) -1
while s<e:
    l[s], l[e] = l[e], l[s]
    s = s + 1
    e = e-1

print(l)"""

"""l = [1, 2, 3, 4, 5]
x = int(input("enter step : "))

d = [l[i] for i in range(x,len(l))]
for i in range(0,x):
    d.append(l[i])

print(d)"""

l = [116,567,890,876,543,678,908,609,709,893,456,678,542,432,136,952,259,642]
x = int(input("enter step : "))
n = len(l)
x %= n
l[0:x] = reversed(l[0:x])
l[x:n] = reversed(l[x:n])
l[0:n] = reversed(l[0:n])
print(l[0:n])