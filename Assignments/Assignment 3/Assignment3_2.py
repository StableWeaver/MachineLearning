import math
n=int(input("Enter no of elements"))
arr=list()
for i in range(n):
    arr.append(input("Enter "+str(i+1)+" element? "))
    
    print()

max=-(math.inf)
for i in arr:
	if(int(i)>max):
		max=int(i)

print("\nThe max is ",max)