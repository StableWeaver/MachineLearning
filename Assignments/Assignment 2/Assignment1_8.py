x=int(input("Enter a number?"))
y=1
for i in range(1,x+1,1):
    for j in range(1,y+1,1):
        print(j,end=' ')
    print()
    y+=1    