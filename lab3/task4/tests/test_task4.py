import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import start_time_memory, end_time_memory, generate_segments
from lab3.task4.src.task4 import count_points_in_segments


class TestCountPointsInSegments(unittest.TestCase):
    def test_should_count_segments(self):
        # given
        test_cases = [
            (([[1, 5], [2, 7], [4, 6]], [1, 4, 6, 9]), [1, 2, 1, 0]),
            (([[0, 2], [1, 3], [2, 4]], [0, 1, 2, 3, 4]), [1, 2, 1, 1, 0]),
            (([], [1, 2, 3]), [0, 0, 0]),
            (([[1, 3]], [1, 2, 3, 4]), [1, 1, 0, 0]),
            (([[1, 10], [5, 15], [0, 20]], [1, 5, 10, 15, 20]), [2, 2, 2, 1, 0]),
            (([[1, 5], [3, 7]], [2, 6, 8]), [1, 1, 0]),
            (([[0, 1], [2, 3], [4, 5]], [0, 2, 4, 6]), [1, 0, 1, 0]),
            (([[1, 5], [1, 5], [1, 5]], [2, 3, 4]), [3, 3, 3]),
            (([[1, 3], [2, 4], [3, 5]], [2, 3, 4]), [1, 2, 1]),
        ]

        # when
        result = [count_points_in_segments(data[0], data[1])
                  for data, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_max_data(self):
        # given
        points = [random.randint(-10 **  8, 10 ** 8) for _ in range(50000)]
        segments = generate_segments(5000)
        start_time, start_memory = start_time_memory()

        # when
        count_points_in_segments(segments, points)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
