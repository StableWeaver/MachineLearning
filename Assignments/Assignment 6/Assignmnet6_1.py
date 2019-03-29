class Demo:
    value=0

    def __init__(self,n1,n2):
        self.no1=n1
        self.no2=n2

    def Fun(self):
        print("1st no={} 2nd no={}".format(self.no1,self.no2))

    def Gun(self):
        print("1st no={} 2nd no={}".format(self.no1,self.no2))    


Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

