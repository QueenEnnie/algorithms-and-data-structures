import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task13.src.task13_2 import LinkedQueue, complete_operations


class TestLinkedQueue(unittest.TestCase):
    def test_should_complete_operation_function(self):
        # given
        operations = ["+ 1", "+ 2", "-", "+ 3", "-"]
        expected_result = [1, 2]
        start_time, start_memory = start_time_memory()

        # when
        result = complete_operations(operations)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)

    def test_should_time_big_data(self):
        # given
        start_time, start_memory = start_time_memory()

        # when
        queue = LinkedQueue()
        for i in range(10 ** 6):
            queue.enqueue(10 ** 9)
        for i in range(10 ** 6):
            queue.dequeue()
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


    def test_should_class_methods_enqueue_dequeue(self):
        # given
        start_time, start_memory = start_time_memory()
        expected_result1 = 1
        expected_result2 = 2
        expected_result3 = 3

        # when
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        result1 = queue.dequeue()
        result2 = queue.dequeue()
        result3 = queue.dequeue()
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)

if __name__ == "__main__":
    unittest.main()
