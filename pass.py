from PyPDF2 import PdfFileWriter, PdfFileReader
import datetime
import os
def securepdf(filepath, password):
    try:
        out = PdfFileWriter()
        file=PdfFileReader(filepath)
        num=file.numPages
        for ind in range(num):
            page=file.getPage(ind)
            out.addPage(page)
        out.encrypt(password)
        t=datetime.datetime.now().time()
        m=str(t.minute)
        s=str(t.second)
        ms=str(t.microsecond)
        with open('encrypted_'+m+'_'+s+'_'+ms+'_.pdf',"wb") as f:
            out.write(f)
    except:
        print("Oops!! Error occured try again")

if __name__=="__main__":
    i=int(input("Enter Number of files to encrypt: "))
    while(i !=0):
        file=input("Path of File: ")
        key=input("Password: ")
        securepdf(file, key)
        i=i-1
