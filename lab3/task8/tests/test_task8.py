import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import start_time_memory, end_time_memory
from lab3.task8.src.task8 import find_closet_to_origin


class TestClosestToOrigin(unittest.TestCase):
    def test_should_find_closest_to_origin(self):
        # given
        test_cases = [
            ([(1, 2), (2, 2), (3, 3)], 2, [(1, 2), (2, 2)]),
            ([(5, 5), (1, 1), (0, 0)], 1, [(0, 0)]),
            ([(1, 0), (0, 1), (-1, 0), (0, -1)], 3, [(-1, 0), (0, 1), (0, -1)]),
            ([(1, 1), (2, 2), (3, 3)], 0, []),
            ([], 2, []),
            ([(3, 4), (6, 8), (1, 1)], 2, [(1, 1), (3, 4)]),
            ([(0, 0)], 1, [(0, 0)]),
            ([(1, 1), (1, -1), (-1, -1), (-1, 1)], 4, [(-1, -1), (1, -1), (-1, 1), (1, 1)]),
            ([(-3, -4), (0, 0), (5, 12)], 2, [(0, 0), (-3, -4)]),
            ([(10, 10), (5, 5), (2, 2)], 3, [(2, 2), (5, 5), (10, 10)]),
        ]

        # when
        result = [find_closet_to_origin(points, number_out)
                  for points, number_out, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])

    def test_should_max_data_time(self):
        # given
        points = [(random.randint(-10 ** 9, 10 ** 9), random.randint(-10 ** 9, 10 ** 9))
                  for _ in range(10 ** 5)]
        number = random.randint(10 ** 3, 10 ** 5)
        start_time, start_memory = start_time_memory()

        # when
        find_closet_to_origin(points, number)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        #then
        self.assertLessEqual(end_time, 10)
        self.assertLessEqual(end_memory, 256)

if __name__ == "__main__":
    unittest.main()
