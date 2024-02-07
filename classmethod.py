'''
self in oops - they take an argument and that argument will extract the information from it.
class atibute are static in nature.
----------------------------------------------------->
class method-stepping stone for factory design pattern.
------------------------------------------------------>
very important:
'''
class player:
    def __init__(self,name,age):
        print("Ctor called")
        self.name=name
        self.age=age
    def get_details(self):
        print(f"name is {self.name}\n Age is {self.age}")

    @classmethod
    def createplayer(cls,fname,lname,age):
        print(f"factory..........")
        return cls(f"{fname} {lname}",age) #calls the constructor

ply1=player("Sachin",37)
ply1.get_details()

print("-"*60)
ply2=player.createplayer("Virat","Kohli",36)
ply2.get_details()