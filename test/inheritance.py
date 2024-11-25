# types of inheritance
# 1. single inheritance

"""class Phone:
    def __init__(self,price,brand,camera):
        print("inside parent constructor ")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone ")


class SmartPhone(Phone):
    pass


SmartPhone(1000, "apple", "13px").buy()"""


# multilevel inheritance
"""class Product:
    def review(self):
        print("product customer review")


class Phone(Product):
    def __init__(self,price,brand,camera):
        print("inside parent constructor ")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone ")


class SmartPhone(Phone):
    pass


s = SmartPhone(1000, "apple", "13px")
s.buy()
s.review()
"""

# hierarchical inheritance


"""class Phone():
    def __init__(self,price,brand,camera):
        print("inside parent constructor ")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone ")


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    pass


SmartPhone(1000, "apple", "13px").buy()


FeaturePhone(20000,"LAVA", "12PX").buy()"""

# multiple inheritance


"""class Phone():
    def __init__(self,price,brand,camera):
        print("inside parent constructor ")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone ")


class Product:
    def review(self):
        print("customer review")


class SmartPhone(Phone,Product):
    pass


s = SmartPhone(1000, "apple", "13px")
s.buy()
s.review()"""


"""class Phone():
    def __init__(self,price,brand,camera):
        print("inside parent constructor ")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone ")


class Product:
    def buy(self):
        print("buying a product")


class SmartPhone(Product,Phone): # method resolution order (M R O) using this method python decide which parent class to be executed first
    pass


s = SmartPhone(1000, "apple", "13px")
s.buy()"""

# in this code method is calling itself again and again so the loop is infinite So it break the loop and throw an error
"""class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        val = super().m1() + 30
        return val


class C(B):
    def m1(self):
        val = self.m1()+20 # m1 is calling itself again and again
        return val


obj = C()
print(obj.m1())"""







