#Different ways of creating a dictionary.
d1=dict()
print(f"empty dictionary:{d1}")
print(type(d1))

print("-"*60)
d2={'name':'Sachin','runs': 85,'age':32,'oppn':"aus"}
print(f"d2:{d2}")
print(type(d2))

d3=dict({'bookid':'B101','name':'Learning python','price':750,'publication':'orielly'})
print(type(d3))
print(f"d3:{d3}")

d4=dict([('name','Rahul'),('age',34),('runs',45),('opponent','SA')])
print(f"d4;{d4}")
print(type(d4))

d5=dict(name='Sachin',age=36,runs=60,opponent='England')
print(f"d5:{d5}")
print(type(d5))

print("-"*60)
#create
player=dict(name='Sachin',age=36,runs=98,opponent='WI')
print(f"Player:{player}")
#read
print('name:',player['name'])
print('age:',player['age'])
print('runs:',player['runs'])
print('opponent:',player['opponent'])

print("-"*60)
for x in player:
    print(x)#only print the keys
    print(x+"=>"+str(player[x]))#print the key value.

#how to update the dictionary
print("-"*60)
player['runs']=105
player['name']="Riashabh"
player['age']=25
player['venue']='eden garden'
player['year']=2020
print(f"player info:{player}")

#how to delete a key
del player['age']
del player['year']
print(f"after deletion:{player}")

print("-"*60)
print(dir(player))