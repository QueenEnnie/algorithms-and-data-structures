import unittest
from lab3.utils import print_time_memory, start_time_memory, read_from_file
from lab3.task3.src.task3 import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):
    def test_should_scarecrow_sort_from_file(self):
        start_time, start_memory = start_time_memory()

        data = read_from_file()
        step = int(data[0].split()[1])
        numbers = list(map(int, data[1].split()))
        result = "ДА" if scarecrow_sort(numbers, step) else "НЕТ"

        print_time_memory("test_should_merge_sort_from_file",
                          start_time, start_memory)
        self.assertEqual(result, "ДА")

    def test_should_scarecrow_sort(self):
        start_time, start_memory = start_time_memory()
        numbers = [2, 1, 3]
        step = 2
        result = "ДА" if scarecrow_sort(numbers, step) else "НЕТ"
        print_time_memory("test_should_scarecrow_sort",
                          start_time, start_memory)
        self.assertEqual(result, "НЕТ")



if __name__ == "__main__":
    unittest.main()
