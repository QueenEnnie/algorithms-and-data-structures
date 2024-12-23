import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import start_time_memory, end_time_memory
from lab1.task5.src.task5 import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_should_selection_sort(self):
        # given
        test_cases = [
            ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),
            ([1, 4, 2, 3], [1, 2, 3, 4]),
            ([10, 9, 8, 7, 6], [6, 7, 8, 9, 10]),
            ([1], [1]),
            ([], [])
        ]
        # when
        result = [selection_sort(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        start_time, start_memory = start_time_memory()

        # when
        selection_sort(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
