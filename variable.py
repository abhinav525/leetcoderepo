glbx=100
def fun(i):
    print(f"i:{i}")
    j=50
    print(f"j:{j}")
    print(f"glbx:{glbx}")
print(f"before :{glbx}")
fun(50)
print(f"after :{glbx}")
# rule for non local varible is that only local varible can be converted as nonlocal variable.
# global cant be converted to non local variable.
