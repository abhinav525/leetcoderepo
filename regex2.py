import re
st="bait"
res=re.search(r'b.t',st)
if res:
    print("match found\n")
    print(res.group(0))
else:
    print("match not found")