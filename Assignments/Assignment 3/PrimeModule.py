#prime module
from math import sqrt

def prime(n):
    if(n>2 and n%2==0):
        return False
    for i in range(3,int(sqrt(n)+1),2):
        if(n%i==0):
            return False
    return True

#print(prime(int(input("Enter a no to check prime?"))))
