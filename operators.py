'''
Operators


'''
print("Arithmatic Operators")
print(f"10+3={10+3}")
print(f"10-3={10-3}")
print(f"10*3={10*3}")
print(f"10/3={10/3}")
print(f"10//3={10//3}")
print(10%3)
print(10**3)

print("-"*50)
print("Augmentor Operator")
x=10
print(x)
x+=5
print(x)
x/=3
print(x)

print("-"*50)
print("Comparison Operator")
a=10
b=15
print(a==b)
print(a>b)
print(a<b)

print("-"*50)
print("Logical Operators")
# and or not
print(f"1===1 and 2==2 :{1==1 and 2==2}")
print(f"1===2 and 2==1 :{1==2 and 2==1}")
print(f"1===1 or 2==2 :{1==1 or 2==2}")
print(f"1===2 or 2==1 :{1==2 or 2==1}")


print("-" * 50)
print(f"ord('a'):{ord('a')}") # asci value of char. int representation of unicorn char
print(f"ord('A'):{ord('A')}")

print("-" * 50)
print("BITWISE OPERATORS")
print(f"5|3:{5|3}") #or operator
print(f"5&3:{5&3}") # and operator
print(f"5^3:{5^3}") # xor operator
print(f"5<<1:{5<<1}") #left shift operator trick is number * 2^n
print(f"8<<1:{8<<1}") 
print(f"8>>1:{8>>1}") # right shift trick is n/2^n

print("-"* 50)
print("TERNARY OPERATOR")
a=10
print("Abhinav" if a>18 else "mishra")

