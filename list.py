from ast import Index


l1=list()
print(type(l1))#l1 is the object of class list
print(f"l1:{l1}")

print("*"*100)
l2=[1,2,3,4,'five','six','seven','eight',9.0,10.2,11.5,12.7,True,False,3+4j,5-8j]
print(f"l2:{l2}")

print("*"*100)
l3=list(range(1,11))
print(f"l3:{l3}")
print(type(l3))

print("*"*100)

#CRUD Operation in the list
'''
1.Create new list 
'''
l1=list(range(1,11))
print(f"l1:{l1}")
print(type(l1))
#read
print(f"l1[0]:{l1[0]}")
print(f"l1[6]:{l1[6]}")

#iterate
for i in l1:
    print(i,end=" ")
print()

print("*"*100)
#iterate
for i in range(0,len(l1)):
    print(f"l1[i]:{l1[i]}")
print()

#update - modify or add new
print(f"l1:{l1}")
#add new element
l1[4]=500
l1[7]=800
print(f"after addtion of elements l1:{l1}")

#delete
print(f"l1:{l1}")
del l1[3]
del l1[7]
print(f"after deletion in l1:{l1}")

print("-"*60)
print(f"l1:{l1}")
#l1[15]=150 error index out of range because list are static.
#print(f"l1:{l1}")
print(dir(l1))# all the funciton of the list.

print("-"*60)
print("Append")
l1=list(range(1,6))
print(f"l1:{l1}")
print(type(l1))
l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1:{l1}")
#l1.append(9,10,11,12,13)#this will take the list as argument.
print(f"l1:{l1}")
#print(f"l1[9]:{l1[8][0:4]}")#this will print the argument list elements.

print("-"*60)
#extend.
l2=list(range(5,11))
print(f"l2:{l2}")
l2.extend([10,11,12,13,14,15])
print(f"l2:{l2}")
l2.extend(list(range(16,21)))# we can give the list as argument with range function.
print(f"l2:{l2}")

#insert the element at the begning and the middle
print("-"*60)
l1=[3,4,5]
print(f"l1:{l1}")
print(type(l1))
l1.insert(0,0)
print(f"l1:{l1}")

l1.insert(1,1)
l1.insert(2,2)
print(f"l1:{l1}")

#pop
print("-"*60)
l1=list(range(1,21))
print(type(l1))
print(f"l1:{l1}")
l1.pop(2)# will take index as argument.
print(f"l1:{l1}")
res=l1.pop(4)# will print the popped element
print(f"res:{res}")
print(f"l1:{l1}")

res=l1.pop()# if do not give any argument it will remove last element.
print(f"res:{res}")
print(f"l1:{l1}")

# remove
print("-"*60)
l1=[3,1,1,1,1,1,2,3,2,2,2,2,2,1,2,3,1,1,1,1,1,2,3,1,1,1,1,1,2,2,2,3]
l1.remove(3)# will remove the first 3 from the left
print(f"l1:{l1}")

l1.remove(3)#will remove second element from the list from left.
print(f"l1:{l1}")

'''
l1.remove(5)
print(f"l1:{l1}")
error will be file not find as element is not present in the list.
'''

'''

use remove form the list
---------------------------
remove,pop
use remove funciton and remove all 1 l1
use pop function and remove all 2 in l1

'''
print("-"*100)
l1=[1,1,1,1,1,3,2,2,2,2,2,2,2,1,2,3,1,1,1,1,1,2,3,1,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
#print(f"l1:{l1}")
#for i in range(0,len(l1)):
    #l1.remove(1)
    #print(f"l1:{l1}")
#print()

l3=[1,1,1,1,1,3,2,2,2,2,2,2,2,1,2,3,1,1,1,1,1,2,3,1,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
print(f"l3:{l3}")
#for i in range(0,len(list)):
   # while(i>len):
        #print(f"l1:{l1}")
#print()
while(1 in l3):
    l3.remove(1)
    print(f"l3:{l3}")

#pop fun to remove all the 2
'''
for i in range(0,len(list(l3))):
    if(l3[i]==2):
        l3.pop(l3.index(2))
        print(f"l3:{l3}")
print()
'''
print("-"*60)
while(l3.count(2)):
    l3.pop(l3.index(2))
print(f"l3:{l3}")

#Count function
l1=[1,1,1,1,1,3,2,2,2,2,2,2,2,1,2,3,1,1,1,1,1,2,3,1,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
print(f"1 in l1:{l1.count(1)} ")
print(f"3 in l1:{l1.count(3)} ")
print(f"2 in l1:{l1.count(2)} ")

#index function
print("-"*60)
l1=[1,1,1,1,1,3,2,2,2,2,2,2,2,1,2,3,1,1,1,1,1,2,3,1,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
print(l1.index(3))#will print the index of the first index of the element
print(3,l1.index(3)+1)

print("*")
#Copy in Lists:
print("Copy")
l1=[1,2,3,4,5]
print(f"before copy:{l1}")
#copy elements of l1 to l2
l2=l1 #shallow copy ,it copy the data with address.
print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)
print(f"after modification:{l2}")
print(f"l1 after l2 modification:{l1}")# pointing to the same list.
print()

print("-"*60)
print()
# solution of this problem is copy function
l3=[6,7,8,9,10]
print(f"l3 before :{l3}")
# copy from l3 to l4
l4=l3.copy() #deep copy-copies only the values
print(f"l4 before:{l4}")

l4.extend([11,12,13,14,15])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

#flaw in a copy function it is only applicable for top most layer.
print()
print("-"*60)
l5=[10,20,30,40,[1,2,3,4],50]
print(f"l5:{l5}")

#copy l5 to l6
l6=l5.copy()
print(f"l6 before modification:{l6}")
l6[4].extend(list(range(6,11)))
print(f"l6 after modification:{l6}")
print(f"l5 after modification:{l5}")

#to solve this prolem we will use deep copy function
from copy import deepcopy
l7=[2,4,6,[1,3,5,7,9],8,10]
print(f" l7 before:{l7}")
l8=deepcopy(l7)
print(f"l8 before:{l8}")
l8[3].extend([11,13,15,17])
print(f" l8 after:{l8}")#here both the list will not be same.
print(f" l7 after:{l7}")





