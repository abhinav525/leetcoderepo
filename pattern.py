#generate this pattern

'''

generate prime number between 150 to 50 and also print the count of how many prime number

'''

#pattern 1:
'''
1
2 3
4 5 6
7 8 9 0
'''
'''
i=0
j=0
n=int(input("enter the value of n:"))
m=1
for i in range(1,n):
    for j in range(1,i+1):
        if(m==10):
            print(0)
        
        
        else:
            print(m,end="")
            m+=1
    print()
'''
'''      
#pattern 2: 
    



1 2 3 4 5 
 1 2 3 4
  1 2 3 
   1 2 
    1
   2 1 
  3 2 1 
 4 3 2 1
5 4 3 2 1 

'''

for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(2,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

    



        
    
