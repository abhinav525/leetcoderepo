'''
Sort
----
Listprint(f"l1:{l1}")(f"l1:{l1}")-original list will get sorted
sorted(list)-copy of the list, sort it and return it.

'''
l1=[10,4,9,1,6,8,2,5,7]
print(f"l1:{l1}")
l1.sort()
print(f"result:{l1}")

res_desc=sorted(l1,reverse=False)#to print the descending sort
print(f"Descending Order:{res_desc}")

print("-"*60)

l1=[10,'zebra',4,'apple',9,'yellow','blue',1,'violet','green',6,'pink','red',8,'orange','cat',2,'dog','maroon',5,'white',7,3,1,192,1234,29,276]
res=sorted(l1,key=ascii)# this will sort the list based on the ascii value of the alphabet not number.
print(f"l1:{res} ")
'''
l2=[]
for i in range(0,len(l1)):
    if l1[i]==int:
        l2.append()
        print(f"list with the words:{l2}")
        l1.sort()
        print(f" sorted l1 will be:{l1}")
print()
'''
#pass the name  of the function and based in that you can sort that list
# reverse function in list
l1=[10,4,9,1,6,8,2,5,7]
print(f"l1:{l1}")
l1.reverse()
print(f"resverse:{l1}")


