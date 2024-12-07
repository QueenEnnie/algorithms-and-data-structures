import unittest, os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task7.src.task7 import calculating_max


class TestCalculatingMaxInSlidingSequence(unittest.TestCase):
    def test_should_correctness_of_finding(self):
        # given
        data1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        window_size1 = 3
        expected_result1 = [10, 9, 8, 7, 6, 5, 4, 3]

        data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        window_size2 = 3
        expected_result2 = [3, 4, 5, 6, 7, 8, 9, 10]

        data3 = [10, 20, 30, 40]
        window_size3 = 4
        expected_result3 = [40]

        data4 = [1, 5, 3, 6, 4, 2]
        window_size4 = 2
        expected_result4 = [5, 5, 6, 6, 4]

        # when
        result1 = calculating_max(data1, window_size1)
        result2 = calculating_max(data2, window_size2)
        result3 = calculating_max(data3, window_size3)
        result4 = calculating_max(data4, window_size4)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)
        self.assertEqual(result4, expected_result4)

    def test_should_time_big_data(self):
        # given
        data = [random.randint(0, 10 ** 5) for _ in range(10 ** 5)]
        window_size = random.randint(0, 10 ** 3)
        start_time, start_memory = start_time_memory()

        # when
        calculating_max(data, window_size)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 5)
        self.assertLessEqual(end_memory, 512)


if __name__ == "__main__":
    unittest.main()
