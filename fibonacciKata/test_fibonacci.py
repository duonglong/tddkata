import unittest
fibonacci = __import__('fibonacci')


class TestFibonacciAt(unittest.TestCase):
    def test_fibonacci_at_zero(self):
        n0 = fibonacci.fibonacci_at(0)
        self.assertEqual(n0, 0)

    def test_fibonacci_at_1(self):
        n1 = fibonacci.fibonacci_at(1)
        self.assertEqual(n1, 1)

    def test_fibonacci_at_2(self):
        n2 = fibonacci.fibonacci_at(2)
        self.assertEqual(n2, 1)

    def test_fibonacci_at_3(self):
        n3 = fibonacci.fibonacci_at(3)
        self.assertEqual(n3, 2)

    def test_fibonacci_at_negative(self):
        self.assertRaises(RuntimeError, fibonacci.fibonacci_at, -1)
