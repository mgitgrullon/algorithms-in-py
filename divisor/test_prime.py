import unittest
from prime import divisors

class TestPrime(unittest.TestCase):
  def test_result(self):
    self.assertEqual(divisors(15), [3, 5])
    self.assertEqual(divisors(12), [2, 3, 4, 6])
    self.assertEqual(divisors(13), "13 is prime")

  def test_type(self):
    self.assertRaises(TypeError, divisors, "12")