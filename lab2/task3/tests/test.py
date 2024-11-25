import unittest
from lab2.utils import *
from lab2.task3.src.task3 import *


class Inversions(unittest.TestCase):
    def test_should_find_inversions_from_file(self):
        start_time, start_memory = start_time_memory()
        data = list(map(int, read_from_file()[1].split()))
        result = merge_sort(data)[1]
        print_time_memory("test_should_find_inversions_from_file",
                          start_time, start_memory)
        self.assertEqual(result, 17)

    def test_should_find_inversions(self):
        start_time, start_memory = start_time_memory()
        data = [38, 27, 43, 3, 9, 82, 10]
        result = merge_sort(data)[1]
        print_time_memory("test_should_find_inversions",
                          start_time, start_memory)
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()
