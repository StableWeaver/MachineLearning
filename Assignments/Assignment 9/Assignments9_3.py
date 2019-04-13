filename=input("Enter File name to be copied?")
try:
    fd=open(filename,encoding="utf-8")
    newfile=open("Demo.txt",encoding="utf-8",mode="x")
    newfile.write(fd.read())
    print("Written")
except FileNotFoundError:
    print("\n\nFile doesn't exist\n\n")
except Exception:
    print("Some other error.")        

#print(fd)