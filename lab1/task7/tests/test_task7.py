import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import start_time_memory, end_time_memory
from lab1.task7.src.task7 import sort_land


class TestSortLand(unittest.TestCase):
    def test_should_sort_land(self):
        # given
        test_cases = [
            ([4, 2, 7, 1, 5], (4, 1, 3)),
            ([10.5, 20.2, 30.1, 40.3, 50.9], (1, 3, 5)),
            ([1.1, 3.3, 2.2, 4.4], (1, 2, 4)),
            ([15.5, 10.3, 5.1, 25.8], (3, 1, 4)),
            ([100.0], (1, 1, 1)),
            ([2.2, 3.3, 1.1], (3, 1, 2)),
        ]

        # when
        result = [sort_land(array) for array, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


    def test_should_time_big_data(self):
        # given
        array = list(set([random.uniform(1, 10 ** 3) for _ in range(999)]))
        start_time, start_memory = start_time_memory()

        # when
        sort_land(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
