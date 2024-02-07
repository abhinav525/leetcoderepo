def outerfun(greet):
    #simple curry - the greeting are ready you can wish any player
    def innerfun(gname):
        print(greet,gname)
    return innerfun
outerfun("hello")("sachin")#outer will pass the hello and inner will pass the inner fun

print("-"*60)
EngGrt=outerfun("hello")
HinGrt=outerfun("namaste")
TamilGrt=outerfun("vanakam")

EngGrt("Rahul")
HinGrt("Shami")
TamilGrt("Natarajan")

print("-"*60)

def of(greeting):

    def inner(sep):

        def innermost(gname):
            print(greeting,sep,gname)
        return innermost
    return inner
#-----------------------
enggrt=of("welcome")
tmlgrt=of("vanakam")

engrtsnar=enggrt("-------->")
engrtdar=enggrt("==========>")

tmlgrtsinar=tmlgrt("-------->")
tamgrtdar=tmlgrt("==========>")

engrtsnar("rahul")
engrtdar("sachin")
tmlgrtsinar("ashwin")
tamgrtdar("natrajan")

