import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import start_time_memory, end_time_memory
from lab3.task1.src.task1 import randomized_quick_sort
from random import randint


class TestRandomizedQuicksort(unittest.TestCase):
    def test_should_quicksort_(self):
        # given
        test_cases = [
            ([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10]),
            ([], []),
            ([1], [1]),
            ([5, 5, 5, 5], [5, 5, 5, 5]),
            ([2, 3, 1, 5, 4], [1, 2, 3, 4, 5]),
            ([10, -1, 2, 5, 0, 6, 4, -5], [-5, -1, 0, 2, 4, 5, 6, 10]),
            ([100, 10, 1000, -100, 50], [-100, 10, 50, 100, 1000]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ]

        # when
        result = [randomized_quick_sort(array, 0, len(array) - 1) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_quicksort_big_numbers(self):
        # given
        data = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
        expected_result = sorted(data)
        start_time, start_memory = start_time_memory()

        # when
        result = randomized_quick_sort(data, 0, len(data) - 1)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)



if __name__ == "__main__":
    unittest.main()