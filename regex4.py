#compile and findall uses:
import re
st="""
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
"""
regex=re.compile(r'(t\w+)')
res=re.findall(regex,st)
print(f"res:{res}")
print(f"count:{res.count('the')}")

print("-"*60)
# to find the index of the string that lies between.
st="""
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
the quick brown fox jumps over a lazy dog
"""
for match in re.finditer(r'(t\w+)',st):
    s=match.start()#match is the variable
    e=match.end()
    print(f"the string found between {s} and {e}:{st[s:e]}")
result=re.findall(regex,st)
print(f"res:{res}")
print(f"count:{res.count('the')}")

print("-"*60)
#Sub is like a replace function that replace the exsisting string with the new one.
import re
st="the quick brown fox jumps over thier  lazy dog"
x=re.sub(r't\w+',"THE",st,count=2)# it will find all the stirng starting with t.
print(f"result:{x}")


print("-"*60)
'''
from stories
1.check how many start with t
2.check how many end with e
3.check how many one letter words are there
4.three letter words
'''


