from Lab3 import Calculator, Sum_strategy, Sub_strategy, Mul_strategy, Div_strategy
import unittest

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        calculator_object = Calculator()
        calculator_object.first_number = 11
        calculator_object.second_number = 2
        calculator_object.operation = Sum_strategy()
        self.assertEqual(calculator_object(), 13, "Має вийти 13")

    def test_sub(self):
        calculator_object = Calculator()
        calculator_object.first_number = 25
        calculator_object.second_number = 10
        calculator_object.operation = Sub_strategy()
        self.assertEqual(calculator_object(), 15, "Має вийти 15")

    def test_mul(self):
        calculator_object = Calculator()
        calculator_object.first_number = 6
        calculator_object.second_number = 5
        calculator_object.operation = Mul_strategy()
        self.assertEqual(calculator_object(), 30, "Має вийти 30")

    def test_div(self):
        calculator_object = Calculator()
        calculator_object.first_number = 21
        calculator_object.second_number = 7
        calculator_object.operation = Div_strategy()
        self.assertEqual(calculator_object(), 3, "Має вийти 3")


if __name__ == '__main__':
    unittest.main()