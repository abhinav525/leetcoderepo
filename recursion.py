#recursive call and find the factorial of a number
'''
def fact(n):
    while(n>1):
        return n*fact(n-1)
n=5
res=fact(n)
print(res)
'''

#recursive call to generate the fibonacci series
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print(fibonacci(i),end=" ")
print() 










     


    