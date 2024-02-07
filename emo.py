
def of(greeting):

    def inner(sep):

        def innermost(gname):
            from emojis import emojis
            emojized =emojis.encode(greeting +":"+sep+":"+gname)
            print(emojized)
            
        return innermost
    return inner
#-----------------------
enggrt=of("welcome")
engtgrgrt=enggrt("lion")
engtgrgrt("Abhinav")
'''
tmlgrt=of("vanakam")

engrtsnar=enggrt("-------->")
engrtdar=enggrt("==========>")

tmlgrtsinar=tmlgrt("-------->")
tamgrtdar=tmlgrt("==========>")

engrtsnar("rahul")
engrtdar("sachin")
tmlgrtsinar("ashwin")
tamgrtdar("natrajan")
'''

def fun(*args):
    print(args )
    print("-"*60)
fun()
fun(1)
fun(1,2)
fun(1,2,3)
fun(1,2,3,4)

print("-"*60)
def sum(x,y):
    return x+y
def diff(x,y):
    return x-y

def outerfun(fnc):
    logInfo="Logging into the server"

    def Innerfun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-"*60)
    return Innerfun
inRef=outerfun(sum)
inRef(20,15)
diffref=outerfun(diff)
diffref(20,14)


def callme():
    print(f"apple ooty")
def fun(fnc):
    print("hello")
    fnc()
    print("hi")

    def defineme():
        print(f"orange kanpur")
    return defineme
def funcallback(fnc):
    print("bharat")
    fnc()
    print("india")
funcallback(fun(callme)) 
print('-'*60)
def bankjob(fnc):
    print("logging into the server")
    fnc()
    print("logging out of the server")

def debit():
    print("amount credited into the account")
def withdraw():
    print("amount debited into the account")
bankjob(debit)
bankjob(withdraw)