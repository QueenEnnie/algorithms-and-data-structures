import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import start_time_memory, end_time_memory
from lab6.task4.src.task4 import complete_operations


class TestAssociateArray(unittest.TestCase):
    def test_should_little_reversed_sorted(self):
        # given
        test_cases = [
            (["put a 1", "put b 2", "get a", "get b", "prev b", "next a", "delete a", "get a"],
             ['1', '2', '1', '2', '<none>']),
            (["put x 100", "put y 200", "get x", "next x", "delete x", "get x", "prev y"],
             ['100', '200', '<none>', '<none>']),
            (["put key1 value1", "put key2 value2", "get key1", "next key1", "delete key1", "get key2"],
             ['value1', 'value2', 'value2']),
        ]

        # when
        result = [complete_operations(operations) for operations, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


if __name__ == "__main__":
    unittest.main()
