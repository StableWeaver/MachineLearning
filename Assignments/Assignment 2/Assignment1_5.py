#prime
from math import sqrt

def prime(n):
    if(n>2 and n%2==0):
        return"not prime"
    for i in range(3,int(sqrt(n)+1),2):
        if(n%i==0):
            return "not a prime"
    return n,"is a prime no."

print(prime(int(input("Enter a no to check prime?"))))
