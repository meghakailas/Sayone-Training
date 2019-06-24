#Create a class with functions to add, subtract, multiply and division. Also write unit test for
#each functions.
class Basicmath:
    def __init__(self,val):
        self.val=val
    def __str__(self):
        return str(self.val)
    def __add__(self, other):
        tot=Basicmath(self.val+other.val)
        return tot
    def __sub__(self, other):
        diff=Basicmath(self.val-other.val)
        return diff
    def __mul__(self, other):
        pro=Basicmath(self.val*other.val)
        return pro
    def __floordiv__(self, other):
        quo=Basicmath(self.val//other.val)
        return quo
    def __truediv__(self, other):
        q=Basicmath(self.val/other.val)
        return q



# n1=Basicmath(10)
# n2=Basicmath(20)
# n3=Basicmath(30)
# print(n1+n2+n3)
# print(n1-n2-n3)
# print(n1*n2*n3)
# print(n3//n2)
# print(n3/n2)
