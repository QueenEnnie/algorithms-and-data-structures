import unittest
from lab3.utils import print_time_memory, start_time_memory, read_from_file
from lab3.task3.src.task3 import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):
    def test_should_scarecrow_sort_from_file(self):
        # given
        data = read_from_file()
        step = int(data[0].split()[1])
        numbers = list(map(int, data[1].split()))
        expected_result = "ДА"

        start_time, start_memory = start_time_memory()

        # when
        result = "ДА" if scarecrow_sort(numbers, step) else "НЕТ"

        print_time_memory("test_should_merge_sort_from_file",
                          start_time, start_memory)
        # then
        self.assertEqual(result, expected_result)

    def test_should_scarecrow_sort(self):
        # given
        numbers = [2, 1, 3]
        step = 2
        expected_result = "НЕТ"

        start_time, start_memory = start_time_memory()

        # when
        result = "ДА" if scarecrow_sort(numbers, step) else "НЕТ"

        print_time_memory("test_should_scarecrow_sort",
                          start_time, start_memory)

        # then
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()
