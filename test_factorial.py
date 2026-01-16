import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-3)


if __name__ == "__main__":
    unittest.main()
