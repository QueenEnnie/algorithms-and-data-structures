import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import start_time_memory, end_time_memory, generate_big_data
from lab6.task6.src.task6 import check_numbers


class TestFibonacci(unittest.TestCase):
    def test_should_check_numbers(self):
        # given
        test_cases = [
            ([0, 1, 2, 3, 5, 8, 13, 21], ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]),
            ([4, 6, 7, 9, 10, 12], ["No", "No", "No", "No", "No", "No"]),
            ([34, 55, 89], ["Yes", "Yes", "Yes"]),
            ([1, 4, 11, 23], ["Yes", "No", "No", "No"]),
        ]

        # when
        result = [check_numbers(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_time_big_data(self):
        # given
        data = generate_big_data(10 ** 3, 5000)
        start_time, start_memory = start_time_memory()

        # when
        check_numbers(data)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 128)


if __name__ == "__main__":
    unittest.main()
