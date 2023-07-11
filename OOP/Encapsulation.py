class Base:
    def __init__(self):
        self.a = "I have rights"
        self.b = "and priviledges"
        self.c = "more rights"
        self.d = "and power"

class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)


#create an instance of the paren class
obj1 = Base()
print(obj1.a)
print(obj1.b)
print(obj1.c)
print(obj1.d)