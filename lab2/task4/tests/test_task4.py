import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import start_time_memory, end_time_memory
from lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_should_binary_search(self):
        # given
        test_cases = [
            ([1, 2, 3, 4, 5], 3, 2),
            ([10, 20, 30, 40, 50], 40, 3),
            ([5, 3, 1, 7, 9], 70, -1),
            ([8, 3, 7, 10, 1], 7, 2)
        ]

        # when
        result = [binary_search(array, n) for array, n, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])


    def test_should_time_big_data(self):
        # given
        array = range(10 ** 3)
        start_time, start_memory = start_time_memory()

        # when
        binary_search(array, array[-1])
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
