import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import start_time_memory, end_time_memory
from lab7.task4.src.task4 import longest_common_subsequence


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_should_longest_common_subsequence(self):
        # given
        test_cases = [
            ([1, 2, 3, 4, 5], [1, 3, 5], 3),
            ([1, 2, 3], [4, 5, 6], 0),
            ([1, 2, 3], [1, 2, 3], 3),
            ([1, 2, 3, 4, 5], [2, 4], 2),
            ([7, 8, 9], [7, 8, 9], 3),
            ([], [1, 2, 3], 0),
            ([1, 2, 3], [], 0),
            ([1], [1], 1),
            ([1, 3, 5, 7], [2, 3, 5, 8], 2),
            ([1, 2, 3, 4, 5], [2, 3, 4, 6, 7], 3),
        ]

        # when
        result = [longest_common_subsequence(first, second) for first, second, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])




    def test_should_time_big_data(self):
        # given
        first_array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(100)]
        second_array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(100)]
        start_time, start_memory = start_time_memory()

        # when
        longest_common_subsequence(first_array, second_array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 1)


if __name__ == "__main__":
    unittest.main()
