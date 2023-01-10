class Calc:
    n = 150
   # n1 = 250

    def __int__(self,a,b):
        self.firstNum = a
        self.secondNum = b
        print("default constructor")

    def getData(self):
        print("this is the method in class")

    def Summation(self):
        return self.firstNum + self.secondNum + Calc.n

obj =Calc(2,9)
obj.getData()
print(obj.Summation())

obj1 = Calc(27,3)
obj1.getData()
print(obj1.Summation())
#constructrs r methods automatically  created wen v create obj for a class

#self keywrd is mandatory for calling variable name into method
#instance and cls variable hav diff purpose
#consrtcr name shud be __init__
#no new keywrd is required 4 creating object
#class variables are called with classnmae.varname
#instance var are called with self.varname
#var tat cud changes or varies from obj to obj

#def __init__(Self,a,b):

#INHERITANCE - acquiring pptys of parent class
#to call methods we create objects, this is done by: call classname and ()