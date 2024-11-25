import unittest
from lab2.utils import *
from lab2.task5.src.task5 import majority
from random import randint


def find_majority(array):
    return 1 if max([array.count(elem) for elem in array]) > len(array) // 2 else 0
class Majority(unittest.TestCase):
    def test_should_find_majority_elem_from_file(self):
        start_time, start_memory = start_time_memory()
        data = read_from_file()
        result = majority(data)
        print_time_memory("test_should_find_majority_elem_from_file",
                          start_time, start_memory)
        self.assertEqual(result, find_majority(data))

    def test_should_find_majority_elem(self):
        start_time, start_memory = start_time_memory()
        data = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        result = majority(data)
        print_time_memory("test_should_find_majority_elem_from_file",
                          start_time, start_memory)
        self.assertEqual(result, find_majority(data))

if __name__ == "__main__":
    unittest.main()
