'''
def greet():#function definition should be on top
    print("Greetings : MR.Sachin")
greet()#call
'''


#def greetgstCty(gname,x=100,cty="mumbai"):

def admsn(fname,lname,dob,gender,qualification,location,percentage_marks):
    print(f"First name is :{fname} ")
    print(f"last name is :{lname} ")
    print(f"dob is :{dob} ")
    print(f"qualification is :{qualification} ")
    print(f"gender is :{gender} ")
    print(f"location is :{location} ")
    print(f"percentage of marks is :{percentage_marks} ")
admsn(qualification="M.TECH",dob="15/02/00",lname="Mishra",fname="Abhinav",gender="Male",location="Banglore",percentage_marks="86%")

print("-"*60)
def sum(x,y):
    return x+y
a=10
b=20
print(f"sum of {a} and {b} are:{sum(a,b)}")

print("-"*60)
def Arithmatic_calcu(x,y):
    difference=x-y
    sum=x+y
    product=x*y
    quot=x/y
    return(sum,difference,product,quot)

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
result=Arithmatic_calcu(a,b)
print(result)

#variable length arguments
print("-"*70)
def prodAll(*numbers): #*numbers can accept more than one value it is the list
    print(numbers)
    print(*numbers)
    num=1
    for number in  numbers:
        num*=number 
    return num
res=prodAll(1,2,3,4,5)
print(f"result:{res}")

#dicitonary arguments
def acceptPlyrDet(**details):#** is the dictionary
    print(details)
    for k , v in details.items():
        print(k,"=>",v)
acceptPlyrDet(name="sachin",age=32,runs=102,oppns="SA")# we are passing the dictionary.

print("-"*70)

#to print the comment with the help of function.
def fun():
    "this is a doc string"
    #this is a comment 
    print("Hello world\n")
fun()
print(fun.__doc__)#this is the dunder doc we can print the comment.


print("-"*70)
def fun1(x,y):
    '''
    fuction-fun1(x,y)
    -----------------
    1.if x and y are integers then the result is the sum of the numbers
    2.if x and y are stirng then the result is the concated string.
    3.if x and y are of different data type then throws an error
    '''
    return x+y
print("-"*70)
help(fun1)# this will print the multi and single  line comment.

