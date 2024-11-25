import unittest
from lab3.utils import start_time_memory, print_time_memory, read_from_file
from lab3.task8.src.task8 import find_closet_to_origin


class TestClosestToOrigin(unittest.TestCase):
    def test_should_find_closest_to_origin_from_file(self):
        data = read_from_file()
        number_out = int(data[0].split()[1])
        coordinates = [(int(elem.split()[0]), int(elem.split()[1])) for elem in data[1:]]
        start_time, start_memory = start_time_memory()
        result = find_closet_to_origin(coordinates, number_out)
        print_time_memory("test_should_find_closest_to_origin_from_file",
                          start_time, start_memory)
        self.assertEqual(result, [(3, 3), (-2, 4)])

    def test_should_find_closest_to_origin_first_example(self):
        number_out = 1
        coordinates = [(1, 3), (-2, 2)]
        start_time, start_memory = start_time_memory()
        result = find_closet_to_origin(coordinates, number_out)
        print_time_memory("test_should_find_closest_to_origin_first_example",
                          start_time, start_memory)
        self.assertEqual(result, [(-2, 2)])


if __name__ == "__main__":
    unittest.main()
