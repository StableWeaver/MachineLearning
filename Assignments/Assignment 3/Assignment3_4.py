n=int(input("Enter no of elements"))
arr=list()
for i in range(n):
    arr.append(int(input("Enter "+str(i+1)+" element? ")))
    print()

count=arr.count(int(input("Enter the no to be serached? :")))
print("\nThe frequency of no is {}".format(count))