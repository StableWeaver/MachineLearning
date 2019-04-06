import threading


def small(s):
    count=0
    for i in s:
        if(i.islower()):
           count+=1 
    print("small is {}".format(count))
    
def capital(s):
    count=0
    for i in s:
        if(i.isupper()):
           count+=1 
    print("capital is {}".format(count))
  
def digit(s):    
    count=0
    for i in s:
        if(i.isdigit()):
           count+=1 
    print("digit is {}".format(count))


if __name__=="__main__":		
	#n=input("Enter no?")
    s="My Name is 1234567"
    #w=factset(n)
    small =threading.Thread(name="SMALL",target=small,args=(s,))
    
    #w=factset(n)	
    capital =threading.Thread(name="CAPITAL",target=capital,args=(s,))	
    
	
    digit =threading.Thread(name="DIGIT",target=digit,args=(s,))
    
	
    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()
    print("Small Thread name is: {} and id is: {}".format(small.name,small.ident))
    print("Caital Thread name is: {} and id is: {}".format(capital.name,capital.ident))
    print("Digit Thread name is: {} and id is: {}".format(digit.name,digit.ident))
