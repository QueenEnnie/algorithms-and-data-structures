import unittest, os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task6.src.task6 import ArrayQueue, complete_operations


class TestArrayQueue(unittest.TestCase):
    def test_should_check_correctness(self):
        # given
        data = ["+ 9", "+ 3", "+ 6", "?", "-", "?", "-", "?", "+ 1", "?"]
        expected_result = [3, 3, 6, 1]

        # when
        result = complete_operations(data)

        # then
        self.assertEqual(result, expected_result)


    def test_should_check_big_data_time_memory(self):
        # given
        data = []
        for _ in range(10 ** 6 // 2):
            data.append(f"+ {random.randint(-10 ** 9, 10 ** 9)}")
        for _ in range(10 ** 6 // 4):
            data.append("?")
            data.append("-")
        start_time, start_memory = start_time_memory()

        # when
        complete_operations(data)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)



if __name__ == "__main__":
    unittest.main()
