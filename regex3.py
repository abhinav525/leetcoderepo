# #
# import re
# st="bt"
# res=re.search(r'',st)
# if res:
#     print("match found.....")

# else:
#     print("match not found")

# bt="baaaaaaaaaaaaat"
# result=re.search(r'ba?t',bt)#? find the zero or one occurance of the char ,
# if result:
#     print("match found")
# else:
#     print("not found")

# ct="baaat"
# a=re.search(r'ba{3}t',ct)
# if a:
#     print("match found")
# else:
#     print("not found")

# ct="baaaaaat"
# a=re.search(r'ba{3,6}t',ct)#min 3 times max 6 times.
# if a:
#     print("match found")
# else:
#     print("not found")

# ct="b5t"
# a=re.search(r'b[a-zA-z0   -9]t',ct)
# if a:
#     print("match found")
# else:
#     print("not found")

# ct="bait"
# a=re.search(r'b(oa|ai)t',ct)#min 3 times max 6 times.
# if a:
#     print("match found")
# else:
#     print("not found")

# ct="bbt"
# a=re.search(r'b[aeiou]t',ct)#min 3 times max 6 times.
# if a:
#     print("match found")
# else:
#     print("not found")


# ct="bbt"
# a=re.search(r'b[^aeiou]t',ct)#min 3 times max 6 times.
# if a:
#     print("match found")
# else:
#     print("not found")



# st="sample.py"
# res=re.search(r'\.py$',st)
# if res:
#     print("match found")
# else:
#     print("match not found")

#write a License number validation of - LCNO-KAR-05-2014-0005
#LCNO - no changes
#KAR-KER,APN,TND,TEL,MAH
#05- RTO Office number -01-73 no 00
#[t][u] 
#[0-2][1-9]
#[2014] anything greater than 2000
import re# 0005-0001-9999 (no 0000)
number_plate="LCNO-KAR-73-2016-2310"   
res = re.search(r'LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-(2[0-9]{3})-((?!0000)[0-9]{4})',number_plate)
if res:
    print("match found")
    print(res.group(0))
else:
    print("not found")

print("-"*60)
a="the quick brown fox jumps over a lazy dog"
ru=re.search(r'\w+',a)#add + to match the one or more characters
if ru:
    print("match found")
    print(ru.group(0))
else:
    print("not found")

print("-"*60)
a="the quick brown fox jumps over a lazy dog"
ru=re.search(r'\W+',a,re.I)#will be match found because space is the special character
if ru:
    print("match found")
    print(ru.group(0))
else:
    print("not found")

print("-"*60)
a="the quick brown fox jumps over a lazy dog"
ru=re.search(r'\b(t\w+)',a,re.I)#add + to match the one or more characters
if ru:
    print("match found")
    print(ru.group(0))
else:
    print("not found")

ay="good blood bad blood"
res=re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)',ay)
if res:
    print("match found")
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))

else:
    print("not found")



'''
dd\mm\yyyy
dd-01-31
mm-01-12
yyyy-1900- now

valid
dd/mm/yyyy
dd-mm-yyyy

invalid
dd-mm/yyyy
dd/mm-yyyy

'''
date_regex='01/02/1800'
result=re.search(r'(([0-2][0-9])|30|31)/([0-1][1-2])/(19[0-9][0-9])|(([0-2][0-9])|30|31)-([0-1][1-2])-(19[0-9][0-9])|',date_regex)
if result:
    print("match found")
else:
    print("not found")

'''
how do you iterate in your match very imp
'''

print("-"*60)
a="the quick brown fox jumps over a lazy dog"
ru=re.search(r'fox',a)#add + to match the one or more characters
if ru:
    print("match found")
    print("rejected string:" ,a[:ru.start()])
    print(ru.group(0))
    print("unchecked string:" ,a[ru.end():])
else:
    print("not found")