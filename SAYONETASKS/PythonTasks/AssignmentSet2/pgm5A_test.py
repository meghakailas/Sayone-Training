import unittest
from math import *
import pgm5A

#class for testing add function
class Testclass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(pgm5A.BasicMaths.add(100,50),150)
        self.assertEqual(pgm5A.BasicMaths.add(-15,50),35)
        self.assertEqual(pgm5A.BasicMaths.add(-5, -7), -12)
        self.assertEqual(pgm5A.BasicMaths.add(5, -8), -3)

    def test_sub(self):
        self.assertEqual(pgm5A.BasicMaths.sub(100,50),50)
        self.assertEqual(pgm5A.BasicMaths.sub(500,-50),550)
        self.assertEqual(pgm5A.BasicMaths.sub(50, 50), 0)
        self.assertEqual(pgm5A.BasicMaths.sub(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(pgm5A.BasicMaths.multiply(10,20),200)
        self.assertEqual(pgm5A.BasicMaths.multiply(10,-30),-300)
        self.assertEqual(pgm5A.BasicMaths.multiply(-60, 2),-120)
        self.assertEqual(pgm5A.BasicMaths.multiply(10,-2), -20)


    def test_div(self):
        self.assertEqual(pgm5A.BasicMaths.divide(100,20),5)
        self.assertEqual(pgm5A.BasicMaths.divide(5, 20), 0.25)
        self.assertEqual(pgm5A.BasicMaths.divide(-10, 2), -5)
        self.assertEqual(pgm5A.BasicMaths.divide(60, -5), -12)
        self.assertRaises(ZeroDivisionError,pgm5A.BasicMaths.divide,1,0)







if __name__=='__main__':
    unittest.main()




