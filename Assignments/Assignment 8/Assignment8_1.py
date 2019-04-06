import threading

def printeven():
	print("First even nos=>>>>>>>>>>>>")
	for i in range(1,11,1):
		print(i*2)
		
def printodd():
	print("First odd nos=>>>>>>>>>>>>")
	for i in range(1,11,1):
		print(i*2-1)

if __name__=="__main__":		
	even =threading.Thread(target=printeven)
	odd =threading.Thread(target=printodd)	
	
	even.start()
	odd.start()
	
	even.join()
	odd.join()
	
