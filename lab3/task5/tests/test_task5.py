import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import end_time_memory, start_time_memory
from lab3.task5.src.task5 import find_h_index


class TestHIndexCalculation(unittest.TestCase):
    def test_should_h_index(self):
        # given
        test_cases = [
            ([3, 0, 6, 1, 5], 3),
            ([10, 8, 5, 4, 3], 4),
            ([25, 8, 5, 3, 3], 3),
            ([1, 1, 1, 1, 1], 1),
            ([0, 0, 0, 0], 0),
            ([100, 50, 40, 20, 10], 5),
            ([0], 0),
            ([10], 1),
            ([3, 3, 3, 3], 3),
            ([5, 5, 5, 1], 3),
            ([], 0),
        ]

        # when
        result = [find_h_index(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_h_index_second_example(self):
        # given
        data = [random.randint(0, 1000) for _ in range(5000)]
        start_time, start_memory = start_time_memory()

        # when
        find_h_index(data)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
