import PrimeModule as Pm #chkprime fun
n=int(input("Enter no of inputs"))
l=list()
for i in range(n):
    l.append(int(input("Enter {}th no?".format(i+1))))

#filter using the prime def in Pm
#filter check prime
fl=list(filter(lambda x : Pm.prime(x),l))
print("filtered list is : {}".format(fl))

#map  x*2
ml=list(map(lambda x : 2*x , fl))
print("mapped list is : {}".format(ml))

#reduce max no from list
from functools import reduce
r=reduce(lambda x,y :max(x,y),ml)
print("Max no is : {}".format(r))