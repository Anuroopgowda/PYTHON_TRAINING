class anuroop:
    def __init__(self):
        self.a="a"
        self.b="b"
class anuroop1(anuroop):
    def __init__(self):
        anuroop.__init__(self)
    def add1(self):
        return self.a+self.b

a=anuroop1()
print(a.add1())







