import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.a_calculator = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.a_calculator.addition(1, 1), 2)
        self.assertEqual(self.a_calculator.addition(-1, 1), 0)
        self.assertEqual(self.a_calculator.addition(-1, -1), -2)
        self.assertEqual(self.a_calculator.addition(1, -5), -4)
    
    def test_subtract(self):
        self.assertEqual(self.a_calculator.subtract(1, 1), 0)
        self.assertEqual(self.a_calculator.subtract(-1, -1), 0)
        self.assertEqual(self.a_calculator.subtract(1, -1), 2)
        self.assertEqual(self.a_calculator.subtract(1, 3), -2)

    def test_multiply(self):
        self.assertEqual(self.a_calculator.multiply(2, 3), 6)
        self.assertEqual(self.a_calculator.multiply(2, -3), -6)
        self.assertEqual(self.a_calculator.multiply(-2, -3), 6)
        self.assertEqual(self.a_calculator.multiply(2, 0), 0)
        with self.assertRaises(TypeError):
            self.a_calculator.divide(10, "str") 

        
    
    def test_divide(self):
        self.assertEqual(self.a_calculator.divide(4, 2), 2)
        self.assertEqual(self.a_calculator.divide(5, 2), 2.5)
        self.assertEqual(self.a_calculator.divide(5, 0), None)
        self.assertEqual(self.a_calculator.divide(5, -2), -2.5)
        
        self.assertRaises(TypeError, self.a_calculator.divide, "string", "str")
