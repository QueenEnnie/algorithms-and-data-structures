import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import start_time_memory, end_time_memory
from lab5.task6.src.task6 import complete_operations, HeapPriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_should_check_some_operations(self):
        # given
        operations = ["A 3", "A 4", "A 2", "X", "D 2 1", "X", "X", "X"]
        expected_result = [2, 1, 3, '*']

        # when
        result = complete_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_big_data(self):
        # given
        start_time, start_memory = start_time_memory()

        # when
        priority_queue = HeapPriorityQueue()
        for i in range(10 ** 6 // 3):
            priority_queue.add(10 ** 9, i + 1)
        for i in range(10 ** 6 // 3):
            priority_queue.reduce(i + 1, 10 ** 5)
        for i in range(10 ** 6 // 3):
            priority_queue.remove_min()
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
