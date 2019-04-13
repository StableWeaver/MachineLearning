filename1=input("Enter File name 1")
filename2=input("Enter File name 1")
try:
    fd1=open(filename1,encoding="utf-8")
    fd2=open(filename2,encoding="utf-8")
    x="Fire in the hole"
    y="cover me"
    check=True
    while(1):
        x=fd1.readline()
        y=fd2.readline()
        if(x!=y):
            check=False
            break
        if(x=="" or y==""):
            break

    if(check):
        print("\n\nSuccess\n\n")
    else:
        print("\n\nFailure\n\n")

except FileNotFoundError:
    print("\n\nFile doesn't exist\n\n")
except Exception:
    print("Some other error.")        

#print(fd)