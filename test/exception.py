# to handle exception
"""with open('sample1.txt', 'w') as f:
    f.write("hello world")
try:
    with open("sample2.txt",'r') as f:
        print(f.read())
except:
    print("sorry the file is not found")

"""
# to catch specific exception :
"""try:
    f = open('sample.txt','r')
    print(f.read())
    print(m)
except FileNotFoundError:
    print("file not found")
except NameError:
    print("variable not defined")"""

# else block :
"""try:
    f = open("sample.txt",'r')

except FileNotFoundError:
    print("file is not found ")

except Exception:
    print("there is an error :")

else:
    print(f.read())"""

# finally : this block of code will definitely trigger :
"""try:
    f = open("sample3.txt",'r')
except FileNotFoundError:
    print("file is not found ")

except Exception:
    print("there is an error")

else:
    print(f.read())
finally:
    print("this will print definitely")"""

# raise exception :
""'raise NameError("hello ,hello error testing")'""


"""class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount<0:
            raise Exception('amount can not be negative')
        if self.balance<amount:
            raise Exception("less balance")
        self.balance = self.balance - amount



obj = Bank(1000)
try:
    print(obj.withdraw(10000))
except Exception as e:
    print(e)
else:
    print(obj.balance)"""

# creating own custom exception class :
"""class MyException(Exception):
    def __init__(self, message):
        print(message)


class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise MyException('amount can not be negative')
        if self.balance < amount:
            raise MyException("less balance")
        self.balance = self.balance - amount


obj = Bank(1000)
try:
    print(obj.withdraw(10000))
except MyException as e:
    pass
else:
    print(obj.balance)"""

class SecurityError(Exception):
    def __init__(self,message):
        print(message)

    def logout(self):
        print("logout")
class Google:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device != self.device:
            raise SecurityError("another device detected")
        if email == self.email and password == self.password:
            print('welcome')
        else:
            print("login error")


obj = Google('nitish', 'nitish123@gmail.com',1234, 'android')

try:
    obj.login('nitish123@gmail.com', 1234, 'windows')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print("hello")














