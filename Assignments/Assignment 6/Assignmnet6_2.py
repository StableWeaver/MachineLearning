class Circle:

    PI=3.141592653589

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self,r):
        self.Radius=r
        self.CalculateArea()
        self.CalculateCircumference()

    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def Display(self):
        print("Radius={}\nArea={}\nCircumference={}\n".format(self.Radius,self.Area,self.Circumference))

obj1=Circle()
obj1.Accept(5)
obj1.Display()

obj1=Circle()
obj1.Accept(6)
obj1.Display()
