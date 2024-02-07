print("-"*60)
st="hello world"
print(f"st:{st}")
a="helowrd"
b="abcdefg"

x=st.maketrans(a,b)#maketrans function will change to updated value
#print(f"resTbl:{x}")
res=st.translate(x)
print(f"res:{res}")
'''

st = "hello world"
print(f"st :{st}")

print("-" * 60)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st10] :{st[10]}")

# Reverse Indexing
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

#Slicing
print("-" * 60)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[O:]   :{st[0:]}")
print(f"st[:11] :{st[:11]}")
print(f"st[:] :{st[:]}")

# slicing reverse
print("-" * 60)
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]  :{st[-1::-1]}")
print(f"st[:-12:-1] :{st[:-12:-1]}")
print(f"st[::-1]    :{st[::-1]}")

# write a code to check if the string is a palindrome
st = "malayalam"
res = "True" if st[0:9] == st[-1:-10:-1] else "False"
print(f"res:{res}")

print("-" * 60)
# maketrans and translate

st = "hello world"
print(f"st :{st}")
# length of a and b should be same
a = "helowrd"
b = "HELOWRD"

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print(f"ord('h') :{ord('h')}")
print(f"ord('H') :{ord('H')}")
print(f"ord('e') :{ord('e')}")
print(f"ord('E') :{ord('E')}")

res = st.translate(resTbl)
print(f"res :{res}")

2-

# emulate C style from printf

format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")       # tuple
print(values)

print(format % values)
print("Welcome %s, what a %s player" % ("Sachin",  "superb"))
print("-" * 60)

format = "Welcome %s with a rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.82, "class"))
print(format % ("Sachin", 4.825370, "class"))
print(format % ("Sachin", 4.8253787, "class"))

# unix Shell Syntax
print("-" * 60)
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res =  tmpl.substitute(name = "Rahul", adj="class")
print(res)

# Python string syntax
print("-" * 60)
print("Welcomw {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcomw {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcomw {2}, what a {0} player for {1}".format( "class", "India", "Sachin"))
print("Welcomw {pname}, what a {adj} player for {ctry}".format( adj="class", ctry="India", pname="Sachin"))
print("Welcome {name}, your rating {rating}".format(name="Sachin", rating=4))
print("Welcome {name}, your rating {rating:.3f}".format(name="Sachin", rating=4.8766666))

print("-" * 60)
from math import pi, e
print(f"PI={pi} and Euler's constant = {e}")
print("PI={} and Euler's constant = {} and magic number = {}".format(pi, e, 40585))
print("PI={p:.2f} and Euler's constant = {e:.2f} and magic number = {m}".format(p=pi, e=e, m=40585))

print("-" * 60)
full_name = ["Sachin", "Tendulkar"]
print(full_name)
print("Mr.{name}".format(name = full_name))
print("Mr.{name}".format(name = full_name[0]))
print("Mr.{fname} {lname}".format(fname=full_name[0], lname=full_name[1]))

print("-" * 60)
import math
print(__name__)
print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers = {mod.e}".format(mod=math))

3-
# conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num=36))
print("{num} {num:f} {num:b}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=3681250981))

print("Alignmant".center(50, "-"))
print("{num:10}Sachin".format(num=3))
print("{num:10}Sachin".format(num="Ramesh"))

print("-" * 60)
print("{num:<15} Tendulkar".format(num = "Sachin"))
print("{num:^15} Tendulkar".format(num = "Sachin"))
print("{num:>15} Tendulkar".format(num = "Sachin"))

print("-" * 60)
print("{num:*^30}".format(num="Sachin"))
print("{num:05}".format(num=25))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

4-

l1 = list()
print(l1)
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3,4, 'five', 'six', 'seven', 'eight', 9.2, 10.7, 11.25, 2 + 0j, 2 + 1j ]
print(f"l2 :{l2}")
print(type(l2))
print(f"l2[0] :{l2[0]}")

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

#insert
l1[2] = 25
print(f"l1 :{l1}")

# update
# l1[15] = 150
l1[5] =  500
print(f"l1 :{l1}")

# delete
del l1[3]
print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))

5-

# conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num=36))
print("{num} {num:f} {num:b}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=3681250981))

print("Alignmant".center(50, "-"))
print("{num:10}Sachin".format(num=3))
print("{num:10}Sachin".format(num="Ramesh"))

print("-" * 60)
print("{num:<15} Tendulkar".format(num = "Sachin"))
print("{num:^15} Tendulkar".format(num = "Sachin"))
print("{num:>15} Tendulkar".format(num = "Sachin"))

print("-" * 60)
print("{num:*^30}".format(num="Sachin"))
print("{num:05}".format(num=25))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

6-


# copy function
print("-" * 60)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy from l3 to l4

l4 = l3.copy()              # deep copy - only data gets copied

print(f"l4 before :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)

print(f"l3 after :{l3}")
print(f"l4 after :{l4}")

print("-" * 60)

l5 = [11, 12, 13, 14, [1, 2, 3, 4, 5], 15]
print(f"l5 before :{l5}")

# copy from l5 to l6

l6 = l5.copy()

print(f"l6 before :{l6}")

l6[4].extend([6, 7, 8, 9])

print(f"l5 after :{l5}")
print(f"l6 after :{l6}")

print("-" * 60)

from copy import deepcopy
l7 = [10, 20, 30, [2, 4, 6, 8, 10], 40, 50]
print(f"l7 before :{l7}")

l8 = deepcopy(l7)           # deep copy

print(f"l8 before :{l8}")
l8[3].extend([12, 14, 16])

print(f"l7 after :{l7}")
print(f"l8 after :{l8}")

8-
"""

sort - this will sort the original list
sorted - will return a copy of the sorted list, original list will remain the same (unsorted)

"""

l1 = [8, 10, 1, 6, 2, 9, 4, 5, 3, 7]
print(f"l1 :{l1}")

# Sort the elements of the list

asc_num = sorted(l1)
print(f"the ascending order of numbers is :{asc_num}")

desc_num = sorted(l1, reverse=True)
print(f"The descending order of numbers is :{desc_num}")

print("-" * 60)

l2 = [8,'apple', 'zebra', 10, 'yellow', 'blue', 1, 'white', 'cat', 6, 'violet', 'dog', 2, 'green', 'pink', 9, 'orange', 'mango', 4, 'egg', 'queen', 5, 3, 7, 1009, 123, 1459, 29, 230, 2560, 2210]

print(f"l2 :{l2}")

res = sorted(l2, key=ascii)
print()
print(f"res :{res}")

print("-" * 60)

cities = ['thiruvananthapuram', 'delhi', 'bangalore', 'vishakapatnam', 'ooty', 'pune', 'hyderabad', 'mysore', 'coimbatore', 'chennai']

# sort the list by the length of the city names

res_asc = sorted(cities, key=len)
print(res_asc)

print()
res_desc = sorted(cities, key=len, reverse=False)
print(res_desc)

print("-" * 60)

l1 = [8, 10, 1, 6, 2, 9, 4, 5, 3, 7]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")

9-
import math

l1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print the sum of all numbers

x = 0
for i in l1:
    x += i

print(f"The sum of all number in the list :{x}")

print("=" * 60)

l1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print all even numbers and odd numbers seperately
odd = []
even = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'Even Numbers :{even}')
print(f"Odd Numbers :{odd}")

print("=" * 60)

l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
    # print the largest number in the list

print(f"l2 :{l2}")

temp = 0
for i in range(0, len(l2)-1):
    if l2[i] > temp:
        temp = l2[i]

print(f"The largest number is :{temp}")

# print the smallest number in the list
temp = max(l2)
for i in range(0, len(l2)-1):
    if l2[i] < temp:
        temp = l2[i]

print(f"The smallest number is :{temp}")

# print the second largest number in the list

l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
temp = 0
temp2 = 0
for i in range(0, len(l2)-1):
    if l2[i] > temp:
        temp = l2[i]

temp2 = temp
for i in range(0, len(l2)-1):
    if (l2[1] != temp and l2[i] < temp2):
        temp2 = l2[i]

print(temp2)


# print the second smallest number in the list


l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
temp = max(l2)
temp2 = max(l2)

for i in range(0, len(l2)):
   if l2[i] < temp:
     temp = l2[i]

for i in range(0, len(l2)):
   if l2[i] != temp and l2[i] < temp2:
     temp2 = l2[i]

print(f"The second smallest number is :{temp2}")

9-

# largest

temp = 0
l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]

for i in range(0, len(l2) - 1):
    if l2[i] > temp:
        temp = l2[i]

print(f"The largest number is :{temp}")

print("=" * 60)

import math
temp = math.inf

for i in range(0, len(l2)- 1):
    if l2[i] < temp:
        temp = l2[i]

print(f"The smallest number is :{temp}")



'''


