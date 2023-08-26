class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    def __add__(self,x):
        #eturn f"{self.x+x.x}i +{self.y+x.y}j + {self.z+x.z}k  "
        return Vector(self.x+x.x,self.y+x.y,self.z+x.z)
v1=Vector(1,2,3)
v2=Vector(4,5,6)

print(v1)
print(v2)
print(v1+v2)
print(type(v1+v2))