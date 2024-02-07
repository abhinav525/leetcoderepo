#get function
player=dict(name='rahul',age=31,runs=65,opponent='Pakistan')
print(f"player details:{player}")
print(player.get('opn',"please check the key enterd"))#get use  to check if the key is there or not if not then print none
print(player.get('opponent'))

#keys will get all the key from dictionary
player=dict(name='rahul',age=31,runs=65,opponent='Pakistan')
print(f"player details:{player}")
k=player.keys()
print(k)
for k in player.keys():
    print(k,'=>',player[k])

#values function:
print("values")
player=dict(name='rahul',age=31,runs=65,opponent='Pakistan')
print(f"player details:{player}")
v=player.values()
print(v)
print("-"*60)
#fromkeys
player=dict(name='rahul',age=31,runs=65,opponent='Pakistan')
print(f"player details:{player}")
cities=['blr','chennai','mumbai','del','hyderabad']#you cannot assign the values to the keys.
print(f"cities:{cities}")
res=dict.fromkeys(cities)#fromkeys for values function that return a dictionary
print(f"res:{res}") 
res=dict.fromkeys(cities,24)
print(f"res:{res}")

#setdefault->it will update the new key value pair to the dict if they are not available.
player=dict(name='rahul',age=31,runs=65,opponent='Pakistan')
print(f"player details:{player}")
player.setdefault('name','dravid')#will not change the exsisting value
player.setdefault('age',28)
player.setdefault('team','india')
player.setdefault('venue','chepauk')
print(f"player details:{player}")

#pop function->
player={'name': 'rahul', 'age': 31, 'runs': 65, 'opponent': 'Pakistan', 'team': 'india', 'venue': 'chepauk'}
res=player.pop("age")
res=player.pop("runs")
print(f"player details:{player}")

#res=player.pop()->mandatory to pass the argument

#pop items->prints the last key value pair.
player={'name': 'rahul', 'age': 31, 'runs': 65, 'opponent': 'Pakistan', 'team': 'india', 'venue': 'chepauk'}
print(f"player details:{player}")
res=player.popitem()
print(f"res:{res}")

#update

