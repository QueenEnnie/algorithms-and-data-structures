import unittest
from lab3.utils import read_from_file, start_time_memory, print_time_memory
from lab3.task5.src.task5 import find_h_index


class TestHIndexCalculation(unittest.TestCase):
    def test_should_h_index_from_file(self):
        # given
        data = list(map(int, read_from_file()[0].split(",")))
        expected_result = 3

        start_time, start_memory = start_time_memory()

        # when
        result = find_h_index(data)

        print_time_memory("test_should_h_index_from_file",
                          start_time, start_memory)
        # then
        self.assertEqual(result, expected_result)

    def test_should_h_index_second_example(self):
        # given
        data = [1, 3, 1]
        expected_result = 1

        start_time, start_memory = start_time_memory()

        # when
        result = find_h_index(data)

        print_time_memory("test_should_h_index_second_example",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
