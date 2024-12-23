import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import start_time_memory,  end_time_memory
from lab3.task9.src.task9 import closest_pair


class TestClosestPoints(unittest.TestCase):
    def test_should_find_closest(self):
        # given
        test_cases = [
            ([(0, 0), (1, 1), (2, 2), (3, 3)], 1.414214),
            ([(0, 0), (1, 0), (2, 0), (3, 0)], 1.0),
            ([(0, 0), (0, 1), (0, 2), (0, 3)], 1.0),
            ([(-1, -1), (1, 1), (2, 2), (3, 3)], 1.414214),
            ([(1, 2), (2, 1), (3, 4), (4, 3)], 1.414214),
            ([(0, 0), (0, 1), (1, 0), (1, 1)], 1.0)
        ]

        #when
        result = [closest_pair(points) for points, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])

    def test_should_max_time_data(self):
        # given
        points = [(random.randint(-10 ** 9, 10 ** 9), random.randint(-10 ** 9, 10 ** 9))
                  for _ in range(10 ** 5)]
        start_time, start_memory = start_time_memory()

        # when
        closest_pair(points)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        #then
        self.assertLessEqual(end_time, 10)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
