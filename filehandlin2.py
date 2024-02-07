#writing in  a file
'''
FW=open("myFile.txt","w")
n=input("enter the content")
FW.write(n)
FW.close()

FW=open("myFile.txt","a")
m=input("enter the conetnt:")
FW.write(m+"\n")
FW.close()
'''
#writelines will add multiple lines in the txt file FW.writwlines([l1,l2,l3])
#write a codes to accept the lines from the user until the user says 'no'



ch='yes'
s=""
while(ch!="no"):
    st=input("enter the content:")
    s+=st+"\n"
    ch=input("do you want to continue:")
FW=open("myFile.txt","w")
FW.write(s)
FW.close()