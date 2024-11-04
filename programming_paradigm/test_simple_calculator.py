from simple_calculator import  SimpleCalculator 
import unittest 

class MyTest(unittest.TestCase) :
    def setUp(self) :
        self.calc=SimpleCalculator()
        
    def test_addition(self) :
        self.assertEqual(self.calc.add(1,2),3)
    
    def test_subtract(self) : 
        self.assertEqual(self.calc.subtract(3,2),1)  
        
    def test_multiplication(self) :
        self.assertEqual(self.calc.multiply(4,2),8)    
    
    def test_divide(self) :    
        self.assertEqual(self.calc.divide(4,2),2)
        
if __name__ == "__main__" :
    unittest.main()
