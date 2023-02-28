from pythonBasics.oppsdemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    #def __int__(self): #constructor
     #   Calculator.__init__(self) #callong class

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl(2, 20)
print(obj.getcompletedata())

