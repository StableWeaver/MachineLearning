def fact(n,tail=1):
	if(n==0):
		return tail
	return fact(n-1,n*tail)		

#Tail Recursion
print(fact(int(input("Enter Number for factorial?"))))
    

