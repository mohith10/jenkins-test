import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(4,5), 9)
        self.assertEqual(calc.add(-9,7), -2)
        self.assertEqual(calc.add(3,-3), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(4,5), 20)
        self.assertEqual(calc.multiply(10000,0), 0)
        self.assertEqual(calc.multiply(-1,65), -65)

    def test_sub(self):
        self.assertEqual(calc.subtract(4,5), -1)
        self.assertEqual(calc.subtract(-3,-3), 0)
        self.assertEqual(calc.subtract(12,9), 3)

    def test_divide(self):
        self.assertEqual(calc.divide(14, 7), 2)
        self.assertEqual(calc.divide(9,3), 3)
        self.assertEqual(calc.divide(60,6), 10)
        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()