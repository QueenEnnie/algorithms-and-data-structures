import unittest
from lab2.utils import *
from lab2.task4.src.main import binary_search
from random import randint

DATA = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]

def right_search(array, find_array):
    right_result = list()
    for elem in find_array:
        if elem in array:
            right_result.append(array.index(elem))
        else:
            right_result.append(-1)
    return right_result

class BinarySearch(unittest.TestCase):
    def test_should_binary_search_from_file(self):
        start_time, start_memory = start_time_memory()
        data = read_from_file()
        array = list(map(int, data[1].split()))
        find_array = list(map(int, data[3].split()))
        result = [binary_search(array, elem) for elem in find_array]
        print_time_memory("test_should_binary_search_from_file",
                          start_time, start_memory)
        self.assertEqual(result, right_search(array, find_array))

    def test_should_binary_search(self):
        start_time, start_memory = start_time_memory()
        data = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        find_array = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        result = [binary_search(data, elem) for elem in find_array]
        print_time_memory("test_should_binary_search",
                          start_time, start_memory)
        self.assertEqual(result, right_search(data, find_array))


if __name__ == "__main__":
    unittest.main()
