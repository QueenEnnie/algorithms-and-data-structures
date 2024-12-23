import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.task6.src.task6 import find_maximum_subarray


class TestMaxProfit(unittest.TestCase):
    def test_should_find_max_subarray(self):
        # given
        test_cases = [
            ([(0, 1), (1, 2), (2, 3), (3, -1), (4, 2), (5, -3)], 0, 5, (0, 4, 7)),
            ([(0, 1), (1, 3), (2, -2), (3, 5), (4, -1)], 0, 4, (0, 3, 7)),
            ([(0, -1), (1, -2), (2, -3), (3, -4)], 0, 3, (0, 0, -1)),
        ]

        # when
        result = [find_maximum_subarray(array, low, high) for array, low, high, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][3])


if __name__ == "__main__":
    unittest.main()
