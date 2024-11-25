"""class Shape:
    def area(self, a, b=0):
        if b == 0:
            return 3.14*a*a
        else:
            return a*b


obj = Shape()
print(obj.area(3))"""

# Abstraction
from abc import ABC, abstractmethod


class BankApp(ABC):
    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):
    def mobile_login(self):
        print("login into mobile ")

    def security(self):
        print("connected")


mob = BankApp()
mob.database()