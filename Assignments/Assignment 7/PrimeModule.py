#prime module
from math import sqrt

def prime(n):
    if(n>2 and n%2==0):
        return False
    for i in range(3,int(sqrt(n)+1),2):
        if(n%i==0):
            return False
    return True

def checkperfect(n):
    temp=1
    for i in range(2,int(sqrt(n)+1)):
        #print(temp)
        if(n%i==0):
            temp+=i
            if(i!=n/i):
                temp+=n/i
    if(temp==n):
        return True
    else:
        return False    

def fact(n):
    for i in range(1,int(sqrt(n)+1)):
        #print(temp)
        if(n%i==0):
            print("Factor :{}".format(i))
            if(i!=n/i):
                print("Factor :{}".format(int(n/i)))

def factadd(n):
    temp=1
    for i in range(2,int(sqrt(n)+1)):
        #print(temp)
        if(n%i==0):
            temp+=i
            if(i!=n/i):
                temp+=n/i
    return temp                       


#print(prime(int(input("Enter a no to check prime?"))))
#print(checkperfect(28))
#fact(6)