#class with 2 methods getstring and printstring
class Stringdef:
    def getString(self):
        data=input("Enter String:")
        self.data=data
    def printString(self):
        print("The given data is:", self.data.upper())

obj=Stringdef()
obj.getString()
obj.printString()

