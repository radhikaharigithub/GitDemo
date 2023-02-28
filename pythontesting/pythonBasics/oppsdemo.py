class Calculator:
    num = 100

    def __init__(self, a, b):  #default constructor
        self.num1 = a
        self.num2 = b
        print("I am called automatically when object is created")

    def getData(self):  #method
        print("executing as a method in class")

    def summation(self):
        return self.num1 + self.num2 + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj.getData()
print(obj1.summation())



