n=int(input("Enter no of inputs"))
l=list()
for i in range(n):
    l.append(int(input("Enter {}th no?".format(i+1))))

#filter
fl=list(filter(lambda x : x%2==0,l))
print("even nos are {}".format(fl))

#map()
ml=list(map(lambda x : x*x,fl))
print("Squares are {}".format(ml))

#reduce()
from functools import reduce
rl=reduce(lambda x,y: x+y, ml)
print("summation is {}".format(rl))