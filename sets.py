#Sets.
s1=set()
print(f"s1:{s1}")
print(type(s1))
print("-"*60)
s2={1,2,3,4,5}
print(f"s2:{s2}")
print(type(s2))
print("-"*60)

s1=[1,2,3]
print(dir(s1))

#add
s1=set()
s1.add(5)
s1.add(4)
print(f"s1:{s1}")

#update can add more than one value
s1.update([2,3,4,5])
s1.update([7,8,9])
print(f"s1:{s1}")

#pop remove from starting
res=s1.pop()
print(f"s1:{s1}")
#remove pass values only not index
res=s1.remove(5)
print(f"s1:{s1}")

#discard is also remove will not throw error msg if number is not there in set
s1.discard(1)
print(f"s1:{s1}")
#union function or
#intersection function and
#difference
#symmetric difference ^

#frozenset are immutable  no add or remove function