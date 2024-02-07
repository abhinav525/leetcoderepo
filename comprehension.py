#Comprehension->iterating through a collection using lambda syntax.two types 1.list and dictionary.
l1=list(range(1,11))
print(f"l1:{l1}")
squares=[x**2  for x in l1]
print(f"squares:{squares}")

print("-"*60)
sentence="the quick brown fox jumps over a lazy dog"
words=[word for word in sentence.split()]#.split() use to convert in the list
print(f"words:{words}")

print("-"*60)
fruits=[('apple',285),('orange',80),('grapes',140),('pineapple',70),('banana',55),('guava',90),('watermelon',150),('strawberry',350)]
print(f"fruits:{fruits}")
prices=[fruit for fruit in fruits]
print(f"prices:{prices}")
prices=[fruit[0] for fruit in fruits]
print(prices)

print("-"*60)
prices=[fruit[1] for fruit in fruits]
print(prices)

print("-"*60)
prices=[fruit[1] *0.9 for fruit in fruits]
print(prices)

print("-"*60)
prices=[fruit[1] *0.75 for fruit in fruits]
print(prices)

print("-"*60)
prices=[(fruit[0],fruit[1],fruit[1]*0.9 ,fruit[1]*0.75)  for fruit in fruits]
print(prices)
prices=[(fruit[0],fruit[1],fruit[1]*0.9 ,fruit[1]*0.75)  for fruit in fruits if fruit[1]>100]
print(prices)
 
print("-"*60)
words=[word for word in sentence.split()]
print(words)
words=[word for word in sentence.split() if word!='the']
print(words)

players={'sachin':[350,250,300,400,385],'rahul':[200,300,450,150,185],'sehwag':[300,350,425,360],'sourav':[180,250,200,350,150],'laxman':[345,300,200,150,190],'yuvraj':[190,150,120,250,275]}
print(f"pllayers:{players}")
print("Sachin:",players['sachin'])
print("sachin:",sum(players['sachin']))
scores={k:sum(v) for k,v in players.items()}
print(scores)
scores=[player for player in players.keys()]
print(scores)
scores=[player for player in players.values()]
print(scores)

print("-"*60)
avg_score={name:(lambda scr:sum(scr)/len(scr))(score) for name , score in players.items()}
print(f"avg_score:{avg_score}")

'''
print("-"*60)
def avgScr(scr):
    return sum(scr)/len(scr)

average_score={name:avgScr(scores) for name,score in players.items()}
print(average_score)
'''
print("*"*90)
players={'sachin':[350,250,300,400,385],'rahul':[200,300,450,150,185],'sehwag':[300,350,425,360],'sourav':[180,250,200,350,150],'laxman':[345,300,200,150,190],'yuvraj':[190,150,120,250,275]}
#print(f"pllayers:{players}")
rn=[runs for runs in players.values()]
print(rn)
print("-"*70)
scores=[scr for score in players.values() for scr in score if scr >0]
print(scores)

print("-"*80)
scores={k:[scr for scr in score if scr> 200] for k, score in players.items()}
print(scores)


