from OOPS import  Calc
# how to do inheritance: class childclsnme(parentclsnme) in child class

class child(Calc):
    n2 = 350

    def getFullData(self):
        return self.n + self.n1 + self.n2
obj = child(3,7)
