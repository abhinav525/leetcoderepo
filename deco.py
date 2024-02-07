'''
Nested Function:

'''
def outerfun():
    gname="sachin"

    def innerfun():
        print("abhinav")
        print(f"greetings mr.{gname}")
    return innerfun #hof it is the higher  order function
Inref=outerfun()
Inref()

print("-"*60)
outerfun()()#first () will call outer fun and() will call inner fun

#closure to be continue in the next file closure.py

print('-'*60)
def bankjob(fnc):
    def helper(amt):

        print("logging into the server")
        fnc(amt)
        print("logging out of the server")
    return helper

@bankjob#passing deposit as an argument to the bank job using decorator.
def debit(amt):
    print(f"amount credited into the account:{amt}")
@bankjob
def withdraw(amt):
    print(f"amount debited into the account:{amt}")
#deposit=bankjob(debit)#to replace this we can use @bankjob 
debit(45000)
withdraw(20000)


def outer(fnc):
    def inner(amt):
        import time
        time1=time.time()#it will take time before execution
        print(f"time before execution:{time1}")
        fnc(amt)
        time2=time.time()#after execution
        print(f"time after execution:{time2}")
        print(time2-time1)
    return inner

@outer
def timetaken(tfun):
    
    
    for tfun in range(1,tfun):
        continue

timetaken(100000)
    
'''
dec1
--------
dec2 
d1---------
d2**********
fun-welcome
d2----------
d1-###########


def line(fnc):
    print("-"*60)
def star(x):
    print("*"*60)
def hash(y):
    print("#"*60)
def welcome(a):
    print("Welcome")

@line
def printing(fnc):
    print(f"print the line first:{fnc}")

@star
def printstar(x):
    print(f"print the star:{x}")

@welcome
def printwel(a):
    print(f"print the welcome:{a}")


def line(n):
    def helper():
        print("_"*60)
        n()
        print("#"*60)
    return helper()

def line2(n):
    def helper2():
        print("*"*60)
        n()
        print("_"*60)
    return helper2()

@line
@line2
def fun():
    print("welcome")

'''
def dec1(fnc):
	def helper():
		print("-" * 60)
		fnc()
		print("#" * 60)
	return helper
def dec2(fnc):
	def helper():
		print("*" * 60)
		fnc()
		print("-" * 60)
	return helper
@dec1
@dec2
def fun():
	print("fun-welcome")
fun()



    

    
    
            
            
    
        
        


        



    

