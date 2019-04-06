import threading


def even(s):
    x=0
    for i in s:
        if(i%2==0):
            x+=i                
    print("Adition of even is {}".format(x))
    
def odd(s):
    x=0
    for i in s:
        if(i%2!=0):
            x+=i                
    print("Adition of odd is {}".format(x))    
    
if __name__=="__main__":		
	#n=input("Enter no?")
    s={1,2,3,4,5,6}
	#w=factset(n)
    even =threading.Thread(target=even,args=(s,))
	
	#w=factset(n)	
    odd =threading.Thread(target=odd,args=(s,))	
	
    even.start()
    odd.start()
	
    even.join()
    odd.join()
	
