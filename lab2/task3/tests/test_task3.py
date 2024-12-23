import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import start_time_memory, end_time_memory
from lab2.task3.src.task3 import merge_sort_count


class TestSelectionSort(unittest.TestCase):
    def test_should_count_inversions(self):
        # given
        test_cases = [
            ([4, 2, 7, 1, 5], ([1, 2, 4, 5, 7], 5)),
            ([10, 20, 30, 40, 50], ([10, 20, 30, 40, 50], 0)),
            ([1, 9, 3, 7, 5], ([1, 3, 5, 7, 9], 4)),
            ([5, 2, 8, 1, 3], ([1, 2, 3, 5, 8], 6))
        ]

        # when
        result = [merge_sort_count(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
        start_time, start_memory = start_time_memory()

        # when
        merge_sort_count(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
