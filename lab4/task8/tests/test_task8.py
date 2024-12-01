import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import start_time_memory, print_time_memory, read_from_file
from lab3.task8.src.task8 import find_closet_to_origin


class TestClosestToOrigin(unittest.TestCase):
    def test_should_find_closest_to_origin_from_file(self):
        # given
        data = read_from_file()
        number_out = int(data[0].split()[1])
        coordinates = [(int(elem.split()[0]), int(elem.split()[1])) for elem in data[1:]]
        expected_result = [(3, 3), (-2, 4)]

        start_time, start_memory = start_time_memory()

        # when
        result = find_closet_to_origin(coordinates, number_out)

        print_time_memory("test_should_find_closest_to_origin_from_file",
                          start_time, start_memory)
        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_to_origin_first_example(self):
        # given
        number_out = 1
        coordinates = [(1, 3), (-2, 2)]
        expected_result = [(-2, 2)]

        start_time, start_memory = start_time_memory()

        # when
        result = find_closet_to_origin(coordinates, number_out)

        print_time_memory("test_should_find_closest_to_origin_first_example",
                          start_time, start_memory)

        #then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
