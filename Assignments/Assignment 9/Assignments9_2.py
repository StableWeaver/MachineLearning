filename=input("Enter File name?")
try:
	fd=open(filename,encoding="utf-8")
	print(fd.read())
except FileNotFoundError:
    print("\n\nFile doesn't exist\n\n")

#print(fd)