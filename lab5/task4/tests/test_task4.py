import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import start_time_memory, end_time_memory
from lab5.task4.src.task4 import build_heap


class TestHeapBuild(unittest.TestCase):
    def test_should_little_reversed_sorted(self):
        # given
        array = [6, 5, 4, 3, 2, 1]
        expected_result = [(2, 5), (1, 4), (0, 2), (2, 5)]

        # when
        result = build_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_not_reversed_sorted(self):
        # given
        array = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55]
        expected_result = [(3, 7), (2, 5)]

        # when
        result = build_heap(array)

        # then
        self.assertEqual(result, expected_result)



    def test_should_time_big_data(self):
        # given
        array = list(range(0, 10 ** 6))[::-1]
        start_time, start_memory = start_time_memory()

        # when
        build_heap(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 3)
        self.assertLessEqual(end_memory, 512)


if __name__ == "__main__":
    unittest.main()
