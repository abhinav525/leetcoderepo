#Conversions
print("Conversions")
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))#to convert the string to its different types

print("{val:10} {val:f} {val:b}".format(val=36))

print("-"*60)
print("Alignment")
print("{num:10} Tendulkar".format(num=3))
print("{num:10} Tendulkar".format(num="Sachin"))
print("{num:>10} Tendulkar".format(num="Sachin"))#right
print("{num:^10} Tendulkar".format(num="Sachin"))#center
print("{num:<10} Tendulkar".format(num="Sachin"))#left

print("-"*60)
