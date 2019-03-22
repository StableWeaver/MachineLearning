#prime module
from math import sqrt

#reverse a string using Slice
def reverseString(s):
    x=str()
    #print(len(s))
    for i in range(len(s),0,-1):
        x=x+s[i-1]
    return x    

#counts the length
def countstr(x):
    return len(x.split())

from itertools import permutations
def permut(s):
    l=list()
    s=set(permutations(s))
    
    for perm in list(s): 
         #print (''.join(perm))
         l.append(''.join(perm)) 
    return l

def remchar(x,pos):
    s=x[:pos-1]+x[pos:]
    return s    

# ord()to get ascii value of char
# #chr() to get ascci char from ascii value

def asciisum(x):
    sum=0
    for i in x:
        sum+=ord(i)
    sum/=len(x)    
    return sum              