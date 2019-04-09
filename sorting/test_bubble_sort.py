import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
  def test_sort(self):
    self.assertEqual(bubble_sort(
        [1, 5, 2, 3, 4]), [1, 2, 3, 4, 5], "Expected: [1,2,3,4,5]")
