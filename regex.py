'''
Regular Expression-> are special character 
------------------------------------------
1.single character-> .
2.search at the begning of the string-> ^
3. search at the end of the stirng-> $
4.zero or more occurence ->*
5.zero or one occurance->?
7. exactly n times->{n}
8.atleast n times->{n,}
9.min n times or max m times->{n,m}
10.character class->[]
11.grouping->()
12.alternation (or operation)->|
13.escape- supress the meaning of regex->\

\w-word- aplha numeric characters
\W - non word - special characters
\d-digits->numbers
\D- non digits->non numeric
\s - space->spaces
\S- non space->everything other than space
\b- word boundary
\B- non word boundary
\A-begning of the string
\z-end of the string


Back Tracking-> good luck bad luck
(\w+)\s(\w+)\s(\w+)\s(\2)->\2 means the second grouping is called

dir *.txt ->all files with txt extension will be appeared
dir ? .txt->will give the single character.

my ticket id is 123908 for icici bank 
r 'expression'

'''
# match,search,findall,finditer,compile,sub,
import re
st="this is a sample string"
print(f"st:{st}")
if re.match(r"^this",st):
    print("match found\n")
else:
    print("match not found")

if re.search(r"string$",st): #will work only at the begning then we will use search
    print("match found\n")
else :
    print("match not found")