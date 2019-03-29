import PrimeModule as pm


class Numbers:
    def __init__(self,x):
        self.value=x


    def ChkPrime(self):
        return pm.prime(self.value)

    def ChkPerfect(self):
        return pm.checkperfect(self.value)

    def Factors(self):
        print("Factors================================>>>")
        pm.fact(self.value)

    def SumFactors(self):
        return(pm.factadd(int(self.value))) 

    def Display(self):
        print("{} is a Prime no".format(self.value)) if self.ChkPrime() else print("{} is a not Prime no".format(self.value))
        print("{} is a Perfect no".format(self.value)) if self.ChkPerfect() else print("{} is a not Perfect no".format(self.value)) 
        self.Factors()
        print("Sum of factors is :{}".format(self.SumFactors())) 
        print("\n\n\n")

obj1=Numbers(10)
obj1.Display()

obj2=Numbers(28)
obj2.Display()


obj2=Numbers(31)
obj2.Display()