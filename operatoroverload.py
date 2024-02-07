class player:
    def __init__(self,name,age):
        print("Ctor called")
        self.name=name
        self.age=age
    def __str__(self):#operator overloading.
        return (f"name is {self.name}\n Age is {self.age}")
ply1=player('Rahul',36)
print(str(ply1))#str is the type conversion operator

print("-"*60)
print(ply1)# calls __str__ implicitally.