import unittest, os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import start_time_memory, end_time_memory
from lab7.task1.src.task1 import min_coins_exchange


class MinCoinsAmount(unittest.TestCase):
    def test_should_min_coins_exchange(self):
        # given
        test_cases = [
            (11, [1, 2, 5], 3),
            (7, [1, 3, 4], 2),
            (0, [1, 2, 3], 0),
            (1, [2, 5], -1),
            (15, [1, 2, 5], 3),
            (6, [1, 3, 4], 2),
            (23, [7, 3, 2], 4),
        ]
        # when
        result = [min_coins_exchange(money, coins) for money, coins, _ in test_cases]

        # then
        for i in range(len(result)):
            self.assertEqual(result[i], test_cases[i][2])


    def test_should_time_big_data(self):
        # given
        coins = [random.randint(1, 10 ** 3) for _ in range(100)]
        start_time, start_memory = start_time_memory()

        # when
        min_coins_exchange(10 ** 3, coins)
        end_time, end_memory = end_time_memory(start_time, start_memory)

        # then
        self.assertLessEqual(end_time, 1)


if __name__ == "__main__":
    unittest.main()
