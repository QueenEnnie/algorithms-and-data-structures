import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import start_time_memory, end_time_memory
from lab4.task4.src.task4 import check_brackets


class TestBrackets(unittest.TestCase):
    def test_should_check_correctness(self):
        # given
        data1 = "({[)]})"
        expected_result1 = 4
        data2 = "foo(bar[i);"
        expected_result2 = 10
        data3 = "{{[[()]]}}"
        expected_result3 = "Success"
        data4 = "abc(def[ghi{jkl}mno)pqr]stu"
        expected_result4 = 20
        data5 = "foo(bar[baz]qux)"
        expected_result5 = "Success"

        # when
        result1 = check_brackets(data1)
        result2 = check_brackets(data2)
        result3 = check_brackets(data3)
        result4 = check_brackets(data4)
        result5 = check_brackets(data5)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)
        self.assertEqual(result4, expected_result4)
        self.assertEqual(result5, expected_result5)


    def test_should_check_big_data_time_memory(self):
        # given
        data = "(" * 50000 + ")" * 50000
        expected_result = "Success"
        start_time, start_memory = start_time_memory()

        # when
        result = check_brackets(data)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end_time, 5)
        self.assertLessEqual(end_memory, 256)



if __name__ == "__main__":
    unittest.main()
