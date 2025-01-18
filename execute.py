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
class MyMeta(type):
    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    print(name)


# Output: Initializing class MyClass
