n=int(input("Enter no of elements"))
arr=list()
for i in range(n):
    arr.append(input("Enter "+str(i+1)+" element? "))
    
    print()

sum=0
for i in arr:
    sum+=int(i)
    print(i,end=" ")
print("\nThe sum is ",sum)