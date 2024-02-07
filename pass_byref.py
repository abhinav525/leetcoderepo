def fun(lst):
    print(f"lst:{lst}")
    lst.extend([10,20,30,40,50])
    print(f"after modification:{lst}")
lst=list(range(1,6))
print(f"before call:{lst}")
fun(lst)
print(f"after call:{lst}")