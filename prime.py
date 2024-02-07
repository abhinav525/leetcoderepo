#n = int(input("enter the number from:"))
a=150
j=0
while a>=150:
    k=a
    count=0
    for i in range(2,k):
        if k%i==0:
            count+=1
    if count==0:
        print(k)
        j+=1
    a=a-1
print(j)

