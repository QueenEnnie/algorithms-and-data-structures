import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import start_time_memory, end_time_memory
from lab2.task5.src.task5 import majority


class TestMajority(unittest.TestCase):
    def test_should_majority(self):
        # given
        test_cases = [
            ([3, 3, 4, 2, 4, 4, 2, 4, 4], 1),
            ([3, 3, 4, 2, 4, 4, 2, 4], 0),
            ([1, 1, 2, 2, 3, 3, 4, 4, 4], 0),
            ([1, 1, 1, 1, 2, 2, 2], 1),
            ([5, 5, 5, 5, 6, 6, 6], 1),
        ]

        # when
        result = [majority(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = [random.randint(1, 10 ** 9) for _ in range(10 ** 5)]
        start_time, start_memory = start_time_memory()

        # when
        majority(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
