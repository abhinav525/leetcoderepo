#modules are same as library
gname='Sachin Tendulkar'
sports=['cricket','hockey','football','tennis','badminton','basketball','swimming']
runs={'tests':16500,'odi':12000,'t20':2500}

def greet(guest):
    print(f"greetings m{guest},welcome to the event")
    print("-"*60)

class player:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def get_details(self):
        print(f"name is {self.name}\n age is {self. age}")
        print("-"*60)
    greet("abhishek")

ply1=player('vijay',20)
ply1.get_details
ply2=player('waheed',22)
ply2.get_details
# now we will make a new file to consume this module
