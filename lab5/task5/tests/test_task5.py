import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import start_time_memory, end_time_memory
from lab5.task5.src.task5 import parallel_processing


class TestTaskPlanning(unittest.TestCase):
    def test_should_mini_planning(self):
        # given
        flow_number = 3
        task_number = 6
        array = [2, 2, 2, 2, 2, 2]
        expected_result = [(0, 0), (1, 0), (2, 0), (0, 2), (1, 2), (2, 2)]

        # when
        result = parallel_processing(flow_number, task_number, array)

        # then
        self.assertEqual(result, expected_result)


    def test_should_time_big_datat(self):
        # given
        flow_number = 10 ** 5
        task_number = 10 ** 5
        array = [random.randint(0, 10 ** 9) for _ in range(flow_number)]
        start_time, start_memory = start_time_memory()

        # when
        parallel_processing(flow_number, task_number, array)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 6)
        self.assertLessEqual(end_memory, 512)


if __name__ == "__main__":
    unittest.main()
