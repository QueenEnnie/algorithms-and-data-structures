import unittest
from lab3.utils import start_time_memory, read_from_file, print_time_memory
from lab3.task4.src.task4 import count_points_in_segments


class TestCountPointsInSegments(unittest.TestCase):
    def test_should_count_segments_second_example(self):
        # given
        segments = [[-10, 10]]
        points = [-100, 100, 0]
        expected_result = [0, 0, 1]

        start_time, start_memory = start_time_memory()

        # when
        result = count_points_in_segments(segments, points)

        print_time_memory("test_should_count_segments_second_example",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_segments_from_file(self):
        # given
        data = read_from_file()
        segments = [list(map(int, elem.split())) for elem in data[1:-1]]
        points = list(map(int, data[-1].split()))
        expected_result = [1, 0, 0]

        start_time, start_memory = start_time_memory()

        # when
        result = count_points_in_segments(segments, points)

        print_time_memory("test_should_count_segments_from_file",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
