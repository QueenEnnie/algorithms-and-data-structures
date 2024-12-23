import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import start_time_memory, end_time_memory
from lab2.task10.src.task10 import merge_sort


class TestMergeSortOptimized(unittest.TestCase):
    def test_should_merge_sort(self):
        # given
        test_cases = [
            ([4, 2, 7, 1, 5], [1, 2, 4, 5, 7]),
            ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
            ([1, 9, 3, 7, 5], [1, 3, 5, 7, 9]),
            ([5, 2, 8, 1, 3], [1, 2, 3, 5, 8]),
            ([9, 2, 5, 7], [2, 5, 7, 9]),
        ]

        # when
        result = [merge_sort(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(2 * 10 ** 4)]
        start_time, start_memory = start_time_memory()

        # when
        merge_sort(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
