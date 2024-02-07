l=list(range(1,11))
print(f"l:{l}")
# write the map function to generate the square of the list
sq=list(map(lambda a: a**2,l))#it will take the number and store the squares of the number.
print(f"squares{sq}")#this will print the squares of the number in the list

#conversion of currency from dollars to rupees
expenses=[8500,10000,32000,15000,2500,6000,50000]
print(f"expenses:{expenses}")
ds=list(map(lambda a:a*85,expenses))
print(f"rupees:{ds}")

#sort the months based on calendar
months=['apr','aug','dec','feb','mar','may','nov','oct','jan','jun','sep']
from calendar import month_abbr
print(list(month_abbr))#['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] '' because it uses the 0
res=sorted(months,key=list(map(lambda month:month.lower(),list(month_abbr))).index)
print(f"res:{res}")

#filter function:
lst=list(range(1,25))
print(f"lst:{lst}")
even_num=list(filter(lambda x:x%2==0,lst))
print(even_num)

sentence="the quick brown fox jumps over lazy dog"
words=list(filter(lambda word:word!='the',sentence.split()))
print(words)

#reduce function -> 
from functools import reduce
lst=[9,3,5,7,2,4,10,6]
print(f"lst:{lst}")
res=reduce(lambda x,y:x if x<y else y,lst)
print(res)
res=reduce(lambda x,y:x+y,lst)
print(res)

