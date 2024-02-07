Fl=open("myFile.txt","rb") #rb is read in binary mode
pos=Fl.seek(50,0)
print(f"pos:{pos}")
pos=Fl.seek(100,1)
print(f"pos:{pos}")
pos=Fl.seek(-45,1)
print(f"pos:{pos}")
pos=Fl.seek(0,2)
print(f"this is the file size:{pos}")
Fl.close()
#if u are searching for a word in file then the name is in this byte then file handler is used.