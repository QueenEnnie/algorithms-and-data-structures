import unittest, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.task1.src.task1 import complete_operations


class TestSet(unittest.TestCase):
    def test_should_set(self):
        # given
        test_cases = [
            (["A 5", "A 10", "? 5", "? 10", "D 5", "? 5", "? 10"], ["Y", "Y", "N", "Y"]),
            (["A 1", "A 2", "A 3", "? 1", "? 2", "? 3", "D 2", "? 2"], ["Y", "Y", "Y", "N"]),
            (["A 20", "? 20", "D 20", "? 20", "? 25"], ["Y", "N", "N"]),
            (["A 100", "D 100", "? 100", "? 50"], ["N", "N"]),
        ]

        # when
        result = [complete_operations(data) for data, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][1])


if __name__ == "__main__":
    unittest.main()
