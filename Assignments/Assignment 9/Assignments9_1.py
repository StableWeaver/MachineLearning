filename=input("Enter File name?")
try:
    fd=open(filename,encoding="utf-8")
    print("\n\nFile exist\n\n")
except FileNotFoundError:
    print("\n\nFile doesn't exist\n\n")

#print(fd)