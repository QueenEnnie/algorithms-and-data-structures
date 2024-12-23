import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import start_time_memory, end_time_memory
from lab1.task6.src.task6 import bubble_sort


class TestSelectionSort(unittest.TestCase):
    def test_should_bubble_sort(self):
        # given
        test_cases = [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([0, -1, 2, -3, 4], [-3, -1, 0, 2, 4]),
            ([10, 10, 10, 10], [10, 10, 10, 10]),
            ([1, -5, 3, 7, -2], [-5, -2, 1, 3, 7]),
            ([100, 50, 75, 25, 0], [0, 25, 50, 75, 100]),
            ([], []),
            ([42], [42]),
            ([-10, -20, -30, 0, 10, 5], [-30, -20, -10, 0, 5, 10]),
        ]

        # when
        result = [bubble_sort(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        start_time, start_memory = start_time_memory()

        # when
        bubble_sort(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
