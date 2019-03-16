#factorial
from math import sqrt

def factadd(n):
    temp=1
    for i in range(2,int(sqrt(n)+1)):
        #print(temp)
        if(n%i==0):
            temp+=i
            if(i!=n/i):
                temp+=n/i
    return temp


print(int(factadd(int(input("Enter no to get factorial?")))))