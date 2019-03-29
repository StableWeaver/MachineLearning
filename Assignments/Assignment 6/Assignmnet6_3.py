class Arithmetic:

    

    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self,v1,v2):
        self.value1=v1
        self.value2=v2

    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2

    def Addition(self):
        return self.value1+self.value2    
    
    def Subtraction(self):
        return self.value1-self.value2

    def Display(self):
        print("A={}\nArea={}\nCircumference={}\n".format(self.Radius,self.Area,self.Circumference))

obj1=Arithmetic()
obj1.Accept(6,5)
print("Mult is {}".format(obj1.Multiplication()))
print("Div is {}".format(obj1.Division()))
print("Add is {}".format(obj1.Addition()))
print("Sub is {}".format(obj1.Subtraction()))

obj2=Arithmetic()
obj2.Accept(11,3)
print("Mult is {}".format(obj2.Multiplication()))
print("Div is {}".format(obj2.Division()))
print("Add is {}".format(obj2.Addition()))
print("Sub is {}".format(obj2.Subtraction()))
