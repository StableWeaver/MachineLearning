n=int(input("Enter no of inputs"))
l=list()
for i in range(n):
    l.append(int(input("Enter {}th no?".format(i+1))))
#filter(function,input)
fl=list(filter(lambda x : x>=70 and x<=90,l))
print("Filtered list is : {}".format(fl))

#map(function, input)
ml=list(map(lambda x : x+10,fl))
print("Mapped list is : {}".format(ml))

#reduce(function,input)
from functools import reduce
rl=reduce(lambda x,y : x+y,ml)
print("Product is  : {}".format(rl))