class A:
    def __init__(self):
        self.a=10
    def show(self):
        print("This method present in A class")
        
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=20
    def m1(self):
        print("m1 is a member of B class")
        

obj1=B()
print(obj1.a)
print(obj1.b)
obj1.m1()
obj1.show()