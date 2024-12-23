import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab0.utils import start_time_memory, end_time_memory
from lab0.task2.src.task2 import fib


class TestFibonacciNumbers(unittest.TestCase):
    def test_should_fib(self):
        # given
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
            (15, 610),
            (20, 6765),
        ]

        # when
        result = [fib(n) for n, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_time_big_data(self):
        # given
        number = 45
        start_time, start_memory = start_time_memory()

        # when
        fib(number)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
