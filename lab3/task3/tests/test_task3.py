import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import end_time_memory, start_time_memory
from lab3.task3.src.task3 import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):
    def test_should_scarecrow_sort(self):
        # given
        test_cases = [
            ([3, 1, 4, 1, 5, 9, 2, 6], 2, False),
            ([10, 3, 15, 7, 8, 12, 1, 9], 3, False),
            ([5, 5, 5, 5, 5], 2, True),
            ([1, 2, 3, 4, 5, 6, 7], 4, True),
            ([9, 7, 5, 3, 1], 1, True),
            ([], 3, True),
            ([2, 4, 6, 8, 1, 3, 5, 7], 4, False),
            ([5, 4, 3, 2, 1], 5, False),
            ([1, 3, 5, 2, 4, 6], 2, False),
        ]

        # when
        result = [scarecrow_sort(array, step) for array, step, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])

    def test_should_max_data_time(self):
        # given
        numbers = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
        step = random.randint(1, 10 ** 3)
        start_time, start_memory = start_time_memory()

        # when
        scarecrow_sort(numbers, step)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
