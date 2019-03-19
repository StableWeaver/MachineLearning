import math
n=int(input("Enter no of elements"))
arr=list()
for i in range(n):
    arr.append(input("Enter "+str(i+1)+" element? "))
    
    print()

min=(math.inf)
for i in arr:
	if(int(i)<min):
		min=int(i)

print("\nThe min is ",min)