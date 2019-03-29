class BankAccount:
    ROI=10.5

    def __init__(self,x,y):
        self.Name=x
        self.Amount=y

    def Display(self):
        print("Name is {} and Amount is {}\n".format(self.Name,self.Amount))
        
    def Deposit(self,x):
        self.Amount+=x

    def Withdraw(self,x):
        if(self.Amount>x):
            self.Amount-=x
        else:
            print("Insufficient Funds")    

    def CalculateIntrest(self):
        print("Rate of interest is {}",self.Amount*BankAccount.ROI/100)


obj1=BankAccount("Ashish Surve",500000)
obj1.Display()
obj1.Deposit(3141592653589)
obj1.Display()
obj1.Withdraw(3141592653589)
obj1.Display()