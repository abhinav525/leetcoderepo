'''
immutble
---------
strings
tupple
frozensets

mutable
---------
lists
dictionary

'''
def fun(x):
    print(x)
    x+=10
    print(f"after modification:{x}")
y=100
print(f"y before {y}")
fun(y)
print(f"y after {y}")