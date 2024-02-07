'''
 OOPS
'''
class Player: #P is capital pascal casing
    def runs(self):
        print("runs scored.......")
sachin=Player()
sachin.runs()
print(type(sachin))
print(isinstance(sachin,Player))
print(isinstance(sachin,object))
print(isinstance(sachin,str))#sachin is object not string

print("-"*60)

class Player1:
    def __init__(self):#constuctor.
        print("Player initialized....")
        self.name="Sachin"
        self.age=35

    def get_run(self):
        print("runs scored--------")
sachin=Player1()
sachin.get_run()
sachin.__init__()

print("-"*60)
sourav=Player1()
sourav.get_run()
sourav.__init__()#__init__ is the constructor 


class player2:
    def __init__(self) -> None:
        self.name="Sachin"
        self.age=35
    def get_details(self):
        print("the name of the player is {self.name}\nAge is {self.age}")
ply1=player2()
ply1.get_details()

print("-"*60)

'''
multiple inheritence:
# Dictionaries for communication
p1_dict = {'hello': 'namaskar', 'thankyou': 'shukriyad', 'bye': 'alvida'}
p2_dict = {'namaskar': 'hello', 'shukriyad': 'thankyou', 'alvida': 'bye'}

def communicate(person1_dict, person2_dict):
    while True:
        # Person 1 (English to Hindi)
        p1_input = input("Person 1 (English): ").lower()
        if p1_input == 'bye':
            print("Person 1: Bye")
            break
        if p1_input in person1_dict:
            translated_word = person1_dict[p1_input]
            print(f"Person 1: {translated_word}")
        else:
            print("Person 1: Sorry, I didn't understand.")

        # Person 2 (Hindi to English)
        p2_input = input("Person 2 (Hindi): ").lower()
        if p2_input == 'alvida':
            print("Person 2: Bye")
            break
        if p2_input in person2_dict:
            translated_word = person2_dict[p2_input]
            print(f"Person 2: {translated_word}")
        else:
            print("Person 2: Sorry, I didn't understand.")

# Start the conversation
communicate(p1_dict, p2_dict)

'''

