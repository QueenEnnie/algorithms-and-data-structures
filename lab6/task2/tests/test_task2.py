import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.task2.src.task2 import complete_operations


class TestPhoneBook(unittest.TestCase):
    def test_should_complete_operations(self):
        # given
        test_cases = [
            (["add John 12345", "add Alice 67890", "find John", "find Bob", "del John", "find John"],
             ["12345", "not found", "not found"]),
            (["add Mary 55555", "add Bob 66666", "find Mary", "find Bob", "del Mary", "find Mary"],
             ["55555", "66666", "not found"]),
            (["add Adam 10001", "add Eve 10002", "find Adam", "del Eve", "find Eve"],
             ["10001", "not found"]),
            (["add Charlie 123", "del Charlie", "find Charlie"],
             ["not found"]),
        ]

        # when
        result = [complete_operations(operations) for operations, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


if __name__ == "__main__":
    unittest.main()
