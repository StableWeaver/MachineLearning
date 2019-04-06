import threading
import PrimeModule as pm


def deco_evenfact(fun):
	def updator(n):
		s=fun(int(n))
		x=0
		for i in s:
			if(i%2==0):
				x+=i
				#print(x)	
		print("sum of even fact is {}".format(x))
	return updator		

def deco_oddfact(fun):
	def updator(n):
		s=fun(int(n))
		x=0
		for i in s:
			if(i%2!=0):
				x+=i
				#print(x)	
		print("sum of odd fact is {}".format(x))	
	return updator		

if __name__=="__main__":		
	n=input("Enter no?")
	factset=deco_evenfact(pm.factset)
	#w=factset(n)
	even =threading.Thread(target=factset,args=(n,))
	
	factset=deco_oddfact(pm.factset)
	#w=factset(n)	
	odd =threading.Thread(target=factset,args=(n,))	
	
	even.start()
	odd.start()
	
	even.join()
	odd.join()
	
	print("exit from main")
	
