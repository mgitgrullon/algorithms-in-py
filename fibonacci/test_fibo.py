import unittest
from fibo import fibonacci

class TestFibo(unittest.TestCase):
  def test_result(self):
    self.assertEqual(fibonacci(10), 55, "For F(10) expected: 55")

  def test_type(self):
    self.assertRaises(TypeError, fibonacci, "1")

  def test_value(self):
    self.assertRaises(ValueError, fibonacci, -2)
