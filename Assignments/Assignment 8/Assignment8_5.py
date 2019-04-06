import threading


def t1():
    for i in range(1,51,1):
        print(i,end=" ")
    print("\n\n")
def t2():
    for i in range(50,0,-1):
        print(i,end=" ")
    print("\n\n")  


if __name__=="__main__":		

    t1=threading.Thread(name="Thread1",target=t1)
    	
    t2 =threading.Thread(name="Thread2",target=t2)	
    	
    t1.start()
    t1.join()
    t2.start()
    t2.join()

