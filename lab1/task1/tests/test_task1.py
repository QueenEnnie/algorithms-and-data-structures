import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import start_time_memory, end_time_memory
from lab1.task1.src.task1 import insert_sort


class TestInsertSort(unittest.TestCase):
    def test_should_insert_sort(self):
        # given
        test_cases = [
            ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([10, 9, 8, 7, 6, 5], [5, 6, 7, 8, 9, 10]),
            ([0], [0]),
            ([], []),
            ([1, 0], [0, 1]),
            ([3, 2, 1], [1, 2, 3]),
            ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([5, 4, 5, 3, 2, 3], [2, 3, 3, 4, 5, 5]),
        ]

        # when
        result = [insert_sort(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        start_time, start_memory = start_time_memory()

        # when
        insert_sort(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
