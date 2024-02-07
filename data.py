a=input("enter the first number:")
print(type(a))
print(f"a:{a}")# in the form of string

a=int(input("enter the first number:"))
print(type(a))
print(f"a:{a}")# in the form of string
if(a<10):print(f"a is a single digit number:{a}")

b=int(input("enter the second number:"))
print(f"b:{b}")
print(type(b))

c=int(input("enter the third number"))
print(f"c:{c}")
print(type(c))


if(a>=b and a>=c):
    print(f"a is the greatest :{a}")
elif(b>=a and b>=c):
    print(f"b is the greatest :{b}")
else:
    print(f"c is the greates :{c}")

