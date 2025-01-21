#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# print(type(Node))

# class A(type):
#     def __init__(cls,name):
#         name="anuroop"
#
# class B(metaclass=A):
#     print(name)
#     name="anuroop1"
# class MyMeta(type):
#     def __init__(cls, name, bases, dct):
#         print(f"Initializing class {name}")
#         super().__init__(name, bases, dct)
#
# class MyClass(metaclass=MyMeta):
#     print(name)


# Output: Initializing class MyClass

# for i in range(5):
#     print(i)
# else:
#     print("Loop finished without interruption.")

# from abc import ABC,abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "barke"
#     def move(self):
#         return "4"
# class Bird(Animal):
#     def speak(self):
#         return "sound"
#     def move(self):
#         return "fly"
# b1=Bird()
# d1=Dog()
# print(d1.move())
# print(b1.speak())
from abc import ABC,abstractmethod
# class Bankaccount:
#     def __init__(self,acc_no,acc_hol,balance):
#         self.acc_no=acc_no
#         self.acc_hol=acc_hol
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=amount+self.balance
#
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#
#     def p(self):
#         print(self.balance)
#
# a1=Bankaccount(1,"anu",100)
# a1.deposit(100)
# a1.p()
# a1.withdraw(20)
# a1.p()

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class tri(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         print(self.side*self.side)
# t1=tri(100)
# t1.area()

# lst=[1,2,34,4]
# print(lst.insert(-20,10))
# print(lst)


