import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import start_time_memory, end_time_memory
from lab1.task9.src.task9 import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_should_binary_add(self):
        # given
        test_cases = [
            ("1010", "1101", [1, 0, 1, 1, 1]),
            ("1101", "1011", [1, 1, 0, 0, 0]),
            ("111", "1", [1, 0, 0, 0]),
            ("101010", "1101", [1, 1, 0, 1, 1, 1]),
            ("0", "0", [0]),
            ("1111", "1111", [1, 1, 1, 1, 0]),
            ("110101", "101010", [1, 0, 1, 1, 1, 1, 1]),
        ]

        # when
        result = [binary_addition(a, b) for a, b, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])


    def test_should_time_big_data(self):
        # given
        first = "1" * (10 ** 3 - 2) + "00"
        second = "1" * (10 ** 3 - 2) + "01"
        start_time, start_memory = start_time_memory()

        # when
        binary_addition(first, second)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
