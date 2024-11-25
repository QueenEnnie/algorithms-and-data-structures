import unittest
from lab3.utils import start_time_memory, print_time_memory, read_from_file, quicksort_with_key
from lab3.task9.src.task9 import closest_pair


class TestClosestPoints(unittest.TestCase):
    def test_should_find_closest_from_file(self):
        # given
        data = list(tuple(map(int, elem.split())) for elem in read_from_file()[1:])
        quicksort_with_key(data, 0, len(data) - 1, 0)
        expected_result = 1.414214

        start_time, start_memory = start_time_memory()

        #when
        result = closest_pair(data)

        print_time_memory("test_should_find_closest_from_file",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_closest_second_example(self):
        #given
        data = [(7, 7), (1, 100), (4, 8), (7, 7)]
        expected_result = 0.0

        start_time, start_memory = start_time_memory()

        # when
        result = closest_pair(data)

        print_time_memory("test_should_find_closest_second_example",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
