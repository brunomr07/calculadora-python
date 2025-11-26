import unittest
from calculator import safe_eval

class TestCalculator(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(safe_eval("1+1"), 2)
        self.assertEqual(safe_eval("5-2"), 3)
        self.assertEqual(safe_eval("3*4"), 12)
        self.assertEqual(safe_eval("10/2"), 5)

    def test_advanced_operations(self):
        self.assertEqual(safe_eval("2**3"), 8)
        self.assertEqual(safe_eval("9//2"), 4)
        self.assertEqual(safe_eval("10%3"), 1)

    def test_math_functions(self):
        self.assertAlmostEqual(safe_eval("sqrt(16)"), 4.0)
        self.assertAlmostEqual(safe_eval("sin(0)"), 0.0)
        self.assertAlmostEqual(safe_eval("cos(0)"), 1.0)
        self.assertAlmostEqual(safe_eval("log10(100)"), 2.0)

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            safe_eval("abc")
        with self.assertRaises(ValueError):
            safe_eval("__import__('os').system('rm -rf /')")
        with self.assertRaises(ValueError):
            safe_eval("lambda x: x")

if __name__ == "__main__":
    unittest.main()
