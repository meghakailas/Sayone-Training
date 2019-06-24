#Define a class named Circle which can be constructed by a radius. The Circle class has a
#method which can compute the area

from math import pi
class Circle:
    def getArea(self):
        radius = float(input("Enter radius:"))
        self.radius=radius
        area=float(pi*(self.radius)**2)
        print("Area is :",area)

obj=Circle()

obj.getArea()
