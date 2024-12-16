import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import start_time_memory, end_time_memory
from lab5.task1.src.task1 import check_is_heap


class TestCheckIsHeap(unittest.TestCase):
    def test_should_is_heap_repeated_elements(self):
        # given
        array = [2, 2, 2, 3, 3, 3, 3]
        expected_result = True

        # when
        result = check_is_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_is_heap_valid_small_data(self):
        # given
        array = [1, 3, 2, 6, 5, 4]
        expected_result = True

        # when
        result = check_is_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_is_heap_incorrect_small_data(self):
        # given
        array = [1, 5, 6, 3, 4, 9, 10, 7]
        expected_result = False

        # when
        result = check_is_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_is_heap_max_value_correct(self):
        # given
        array = [2000000000, 2000000000, 2000000000, 2000000000]
        expected_result = True

        # when
        result = check_is_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_big_data_correct(self):
        # given
        array = list(range(1, 10 ** 6 + 1))
        expected_result = True
        start_time, start_memory = start_time_memory()

        # when
        result = check_is_heap(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)

    def test_should_time_big_data_incorrect(self):
        # given
        array = list(range(1, 10 ** 6 + 1))
        array[-1] = 0
        expected_result = False
        start_time, start_memory = start_time_memory()

        # when
        result = check_is_heap(array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
