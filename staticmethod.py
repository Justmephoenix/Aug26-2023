class Math:
    def __init__(self,num):
        self.num=num

    def autonum(self,n):
        self.num=self.num+n



    @staticmethod
    def add(a,b):
        return a+b


a=Math(5)
print(a.num)

a.autonum(10)
print(a.num)
print(a.add(10,12))