print(range(1,10))
l1=list(range(1,10))
print(f"l1:{l1}")#it will print less than 10 not equal to 10

print("-"*60)
l2=list(range(1,11))
print(f"l2:{l2}")

n=int(input("enter the n:"))
l3=list(range(1,n))
print(f"l3:{l3}")

n= int(input("enter n:"))
print("-"*60)
for i  in range(1,n):
    print(i)

print("-" *60)
i=0
for i in range(1,25):
    print(i,end=" ")
print()


print("-" *60)
i=0
for i in range(1,26):
    if(i>20):
        break
    if(i%2==1):
        continue
    print(1,end=" ")
else:
    print("\n   completed the iteration of even numbers")
print()






