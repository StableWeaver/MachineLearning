import PrimeModule as Pm #chkprime fun

n=int(input("Enter no of elements"))
arr=list()
for i in range(n):
    arr.append(int(input("Enter "+str(i+1)+" element? ")))
print()

def ListPrime():
    sum=0
    for i in arr:
        if(Pm.prime(i)):
            #print("{}".format(i))
            sum+=i
    return sum

print("Addition of prime is {}".format(ListPrime()))

