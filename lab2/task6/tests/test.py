import unittest
from utils import *
from lab2.task6.src.main import find_maximum_subarray
from random import randint


def find_majority(array):
    return 1 if max([array.count(elem) for elem in array]) > len(array) // 2 else 0
class MaxProfit(unittest.TestCase):
    def test_should_find_best_sell_buy_days(self):
        start_time, start_memory = start_time_memory()
        data_read = read_from_file()
        data = [[elem.split(",")[2], float(elem.split(",")[4].strip())] for elem in data_read[1:]]
        for i in range(len(data) - 1):
            data[i] = [data[i][0], data[i + 1][1] - data[i][1]]
        buy_day, sell_day, max_profit = find_maximum_subarray(data, 0, len(data) - 1)
        result = f"Фирма: {data_read[1].split(',')[0]}\n"
        f"Период: {data_read[1].split(',')[2]} - {data_read[-1].split(',')[2]}\n"
        f"Дата покупки: {data[buy_day][0]}\n"
        f"Дата продажи: {data[sell_day][0]}\n"
        f"Сумма прибыли: {max_profit}"
        print_time_memory("test_should_find_majority_elem_from_file",
                          start_time, start_memory)
        right_result = f"Фирма: SBER\n"
        f"Период: 231027 - 241025\n"
        f"Дата покупки: 240903\n"
        f"Дата продажи: 241025\n"
        f"Сумма прибыли: 248.66"
        self.assertEqual(result, right_result)


if __name__ == "__main__":
    unittest.main()
