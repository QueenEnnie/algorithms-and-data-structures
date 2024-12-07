import unittest, os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task8.src.task8 import calculate_postfix


class TestCalculatePostfix(unittest.TestCase):
    def test_should_correctness_of_finding(self):
        # given
        data1 = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
        expected_result1 = 14

        data2 = ["1", "2", "+", "3", "+", "4", "+"]
        expected_result2 = 10

        data3 = ["1", "2", "+", "3", "4", "+",
                 "*", "5", "6", "+", "*", "7", "+"]
        expected_result3 = 238

        data4 = ["7"]
        expected_result4 = 7

        # when
        result1 = calculate_postfix(data1)
        result2 = calculate_postfix(data2)
        result3 = calculate_postfix(data3)
        result4 = calculate_postfix(data4)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)
        self.assertEqual(result4, expected_result4)

    def test_should_time_big_data(self):
        # given
        numbers = [str(random.randint(0, 9)) for _ in range(10 ** 6  // 2)]
        operators = random.choices(['+', '-', '*'], k=10 ** 6 // 2 - 1)
        postfix_expression = numbers + operators
        start_time, start_memory = start_time_memory()

        # when
        calculate_postfix(postfix_expression)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 2)
        self.assertLessEqual(end_memory, 256)


if __name__ == "__main__":
    unittest.main()
