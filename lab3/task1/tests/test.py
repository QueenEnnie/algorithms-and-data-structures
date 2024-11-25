import unittest
from lab3.utils import read_from_file, start_time_memory, print_time_memory
from lab3.task1.src.task1 import randomized_quick_sort
from random import randint


class TestRandomizedQuicksort(unittest.TestCase):
    def test_should_quicksort_from_file(self):
        start_time, start_memory = start_time_memory()
        data = list(map(int, read_from_file()[1].split()))
        randomized_quick_sort(data, 0, len(data) - 1)
        print_time_memory("test_should_quicksort_from_file",
                          start_time, start_memory)
        self.assertEqual(data, sorted(data))

    def test_should_quicksort_big_numbers(self):
        data = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
        start_time, start_memory = start_time_memory()
        randomized_quick_sort(data, 0, len(data) - 1)
        print_time_memory("test_should_quicksort_big_numbers",
                          start_time, start_memory)
        self.assertEqual(data, sorted(data))


if __name__ == "__main__":
    unittest.main()
