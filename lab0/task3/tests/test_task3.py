import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab0.utils import start_time_memory, end_time_memory
from lab0.task3.src.task3 import fib_new


class TestFibonacciNumbers(unittest.TestCase):
    def test_should_fib_new(self):
        # given
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 3),
            (8, 1),
            (9, 4),
            (10, 5),
            (15, 0),
            (20, 5),
            (25, 5),
            (30, 0),
        ]

        # when
        result = [fib_new(n) for n, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_time_big_data(self):
        # given
        number = 10 ** 7
        start_time, start_memory = start_time_memory()

        # when
        fib_new(number)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 5)
        self.assertLessEqual(end_memory, 512)


if __name__ == "__main__":
    unittest.main()
