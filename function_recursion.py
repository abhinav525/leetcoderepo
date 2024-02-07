#immutable dicitonary
#this is for the specific object to call and print the specific object. 
from collections import namedtuple
def Arithmatic_calcu(x,y):

    nmdTpl=namedtuple("arithmetic",["sum","difference","product","quot"])#class named arithmatic and attributes are sum,diff,prod,quot
    difference=x-y
    sum=x+y
    product=x*y
    quot=x/y
    res= nmdTpl(sum=sum,difference=difference,product=product,quot=quot)
    return res

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
result=Arithmatic_calcu(a,b)
#print(result)
print(f"sum:{result.sum}")
print(f"product:{result.product}")