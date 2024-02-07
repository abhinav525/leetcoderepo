#formatting
#emulate c style printf
'''
format="Hello  %s what a %s player"
print(format)
values=("Sachin,superb")
print (values)
#print(format % values)
print("Hello  %s what a %s player" % ("Sachin,superb"))

'''
#format strings from python
print("welcome {},what a {} player for {}".format(  "Sachin","super","India"))
print("welcome {pname},what a {adj} player for {cntry}".format(cntry="India",pname="Sachin",adj="super"))