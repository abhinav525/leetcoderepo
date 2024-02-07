import collections
st="abacaaabbbccddabbccabadd"
#how many times each character occurs in the stirng ,put it in a dictionary
res=collections.Counter(st)# to count the occurence of each character.
#counter-
print(res)
'''
count={}
for char in count:
    if char in st:
        count[char]+=1
        print(f"it is present:{st}")
    else:
        count[char]=1
        print(f"it is not present:{st}")
    print(count)
'''
'''
Libraries:
collection 
functiontools
itertools
'''