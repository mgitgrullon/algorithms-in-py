import unittest
from array_diff import array_diff


class TestArrayDiff(unittest.TestCase):
  def test_result(self):
    self.assertEqual(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    self.assertEqual(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    self.assertEqual(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    self.assertEqual(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    self.assertEqual(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
    self.assertEqual(array_diff([-13, 1, 19, -2, 5, -17, 4, 5, 11, 10, 3, 7, -10, -2, -17],[14]), [-13, 1, 19, -2, 5, -17, 4, 5, 11, 10, 3, 7, -10, -2, -17], "expected [-13, 1, 19, -2, 5, -17, 4, 5, 11, 10, 3, 7, -10, -2, -17]")
  
  def test_types(self):
    self.assertRaises(TypeError, array_diff, (-1, -1))


if __name__ == "__main__":
  unittest.main()