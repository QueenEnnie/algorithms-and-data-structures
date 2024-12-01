import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import read_from_file, start_time_memory, print_time_memory
from lab3.task1.src.task1 import randomized_quick_sort
from random import randint


class TestRandomizedQuicksort(unittest.TestCase):
    def test_should_quicksort_from_file(self):
        # given
        data = list(map(int, read_from_file()[1].split()))
        expected_result = sorted(data)

        start_time, start_memory = start_time_memory()

        randomized_quick_sort(data, 0, len(data) - 1)
        # when

        print_time_memory("test_should_quicksort_from_file",
                          start_time, start_memory)

        # then
        self.assertEqual(data, expected_result)

    def test_should_quicksort_big_numbers(self):
        # given
        data = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
        expected_result = sorted(data)

        start_time, start_memory = start_time_memory()
        # when

        randomized_quick_sort(data, 0, len(data) - 1)
        print_time_memory("test_should_quicksort_big_numbers",
                          start_time, start_memory)

        # then
        self.assertEqual(data, expected_result)


if __name__ == "__main__":
    unittest.main()
