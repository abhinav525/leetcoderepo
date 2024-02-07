'''
File handling:

'''
file_path = "C:\\Users\\KIIT\\Desktop\\KPIT PYTHON\\gandhi.txt"

# Open the file in read mode with UTF-8 encoding
Fl = open(file_path, "r", encoding="utf-8")

# Read the contents of the file
#st = Fl.read()
#print(st)

# Close the file
#Fl.close()
#st=Fl.readline()#can read one line
#print(st)
#print(st)

for st in Fl.readlines(100):
    print(st)
Fl.close()
#open a text file  how many times each word is occuring.