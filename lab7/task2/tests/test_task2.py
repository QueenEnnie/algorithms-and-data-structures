import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import start_time_memory, end_time_memory
from lab7.task2.src.task2 import minimal_amount_of_operations


class TestMinimalAmountOfOperations(unittest.TestCase):
    def test_should_min_amount_of_operations(self):
        # given
        test_cases = [
            (1, (0, [1])),
            (2, (1, [1, 2])),
            (3, (1, [1, 3])),
            (4, (2, [1, 3, 4])),
            (5, (3, [1, 3, 4, 5])),
            (6, (2, [1, 3, 6])),
            (10, (3, [1, 3, 9, 10])),
            (15, (4, [1, 3, 4, 5, 15])),
            (18, (3, [1, 3, 9, 18])),
            (19, (4, [1, 3, 9, 18, 19]))
        ]
        # when
        result = [minimal_amount_of_operations(n) for n, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_time_max_data(self):
        # given
        number = 10 ** 6
        start_time, start_memory = start_time_memory()

        # when
        minimal_amount_of_operations(number)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 1)


if __name__ == "__main__":
    unittest.main()
