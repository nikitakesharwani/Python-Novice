
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"
        

class B:
    def __init__(self):
        super().__init__() 
        self.bar = "bar" 
        self.name = "class B"
          
        

class C(B, A):
    def __init__(self):
        super().__init__()

    def showresult(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c = C()
c.showresult()
print(C.__mro__)