#Strings: They are immutable in python
st="Hello world"
print(f"st:{st}")
print(type(st))

print("-"*60)
print(f"st[0]:{st[0]}")
print(f"st[6]:{st[6]}")
print(f"st[10]:{st[10]}")

#reverse indexing
print(f"st[-1]:{st[-1]}")
print(f"st[-5]:{st[-5]}")

print("-"*60)
#Slicing
print(f"st[0:5:1]:{st[0:5:1]}")
print(f"st[6:11:1]:{st[6:11:1]}")
print(f"st[-6:-1:1]:{st[-6:-1:1]}")
print(f"st[-1:-6:-1]:{st[-1:-6:-1]}")

#strings are immutable
st="hello world"
print(f"st:{st}")
print(f"st[0]:{st[0]}")

#functions to manipulate your string:
print("find")
st1="hello world"
st2="the quick brown fox jumps over the lazy dog"
print(f"st1:{st1}")
idx=st1.find("l")#will give the index of where it present.
print(f"index:{idx}")

'''
print("-"*60)
#find and replace
print(f"st1:{st1}")
res=st1.replace("h,H")
print(f"res:{res}")
'''




