# if file is not present
f = open('sample.txt', 'w')  # step 1 open the file
f.write('hello world')  # read/write the file
f.close()  # close the file
# since file is closed
"""f.write('hello world') will not work"""

# write multiple string
f = open('sample1.txt', 'w')
f.write('hello world')
f.write('\nhow are you')
f.close()

# if the file is already present
f = open('sample.txt', 'w')
f.write('salman khan')
f.close()

f = open('sample1.txt', 'a')
f.write('\nI am fine')
f.close()

l = ['hello\n','hi\n','how are you\n','i am fine']
f = open('sample1.txt','w')
f.writelines(l)
f.close()


"""f = open('sample1.txt','r')
while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data,end='')

f.close()"""

"""with open('sample1.txt','w') as f:
    f.write('muskan chaudhary')

with open("sample1.txt",'r') as f:
    print(f.read())"""

"""with open("sample1.txt","r") as f:
    print(f.read(10))
    print(f.read(10))"""

# with help of this code we can read a big file
"""big_l = ["hello world " for i in range(500)]
with open("big.txt",'w') as f:
    f.writelines(big_l)

with open('big.txt','r') as f:
    chunk_size = 10
    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size),end="###")
        f.read(chunk_size)"""

"""with open("sample1.txt",'r') as f:
    f.seek(15)
    print(f.read(12))
    print(f.tell())"""

with open('sample1.txt','w') as f:
    f.write("hello")
    f.seek(0)
    f.write("ma")



