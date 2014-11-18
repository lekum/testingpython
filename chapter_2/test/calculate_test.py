import unittest
from ..calculate import Calculate

class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculate()

    def test_add_method_retuns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_raises_execption_with_strings(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

if __name__ == '__main__':
    unittest.main()
