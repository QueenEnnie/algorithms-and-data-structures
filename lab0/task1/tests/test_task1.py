import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab0.utils import start_time_memory, end_time_memory
from lab0.task1.src.task1_1 import addition
from lab0.task1.src.task1_2 import new_addition


class TestAddition(unittest.TestCase):
    def test_should_addition(self):
        # given
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 300),
            (-5, -5, -10),
            (0, -10, -10),
            (999, 1, 1000),
            (-100, -200, -300),
        ]
        # when
        result = [addition(a, b) for a, b,_ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])

    def test_should_new_addition(self):
        # given
        test_cases = [
            (2, 3, 11),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 40100),
            (-5, -5, 20),
            (0, -10, 100),
            (-100, -200, 39900),
        ]
        # when
        result = [new_addition(a, b) for a, b,_ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])

    def test_should_time_big_data_addition(self):
        # given
        a, b = 10 ** 9, 10 ** 9
        start_time, start_memory = start_time_memory()

        # when
        addition(a, b)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)

    def test_should_time_big_data_new_addition(self):
        # given
        a, b = 10 ** 9, 10 ** 9
        start_time, start_memory = start_time_memory()

        # when
        new_addition(a, b)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
