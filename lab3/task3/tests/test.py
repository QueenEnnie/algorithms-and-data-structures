import unittest
from lab2.utils import *
from lab2.task1.src.task1 import *
from random import randint

DATA = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]

class MergeSort(unittest.TestCase):
    def test_should_merge_sort_from_file(self):
        data = list(map(int, read_from_file()[1].split()))
        start_time, start_memory = start_time_memory()
        result = merge_sort(data)
        print_time_memory("test_should_merge_sort_from_file",
                          start_time, start_memory)
        self.assertEqual(result, sorted(data))

    def test_should_merge_big_numbers_reversed(self):
        start_time, start_memory = start_time_memory()
        data = sorted(DATA)[::-1]
        result = merge_sort(data)
        print_time_memory("test_should_merge_big_numbers_reversed",
                          start_time, start_memory)
        self.assertEqual(result, sorted(data))

    def test_should_merge_big_numbers_sorted(self):
        start_time, start_memory = start_time_memory()
        data = sorted(DATA)
        result = merge_sort(data)
        print_time_memory("test_should_merge_big_numbers_sorted",
                          start_time, start_memory)
        self.assertEqual(result, sorted(data))

    def test_should_merge_big_numbers(self):
        start_time, start_memory = start_time_memory()
        result = merge_sort(DATA)
        print_time_memory(" test_should_merge_big_numbers",
                          start_time, start_memory)
        self.assertEqual(result, sorted(DATA))


if __name__ == "__main__":
    unittest.main()
