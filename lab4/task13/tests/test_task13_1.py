import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task13.src.task13_1 import LinkedStack, complete_operations


class TestLinkedStack(unittest.TestCase):
    def test_should_complete_operation_function(self):
        # given
        operations = ["+ 1", "+ 2", "-", "+ 3", "-"]
        expected_result = [2, 3]
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
        stack = LinkedStack()
        for i in range(10 ** 6):
            stack.push(10 ** 9)
        for i in range(10 ** 6):
            stack.pop()
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)

    def test_should_class_methods_push_pop(self):
        # given
        start_time, start_memory = start_time_memory()
        expected_result1 = 3
        expected_result2 = 2
        expected_result3 = 1

        # when
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        result1 = stack.pop()
        result2 = stack.pop()
        result3 = stack.pop()
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)
        self.assertLessEqual(end_time, 3)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
