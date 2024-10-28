from lab2.utils import *


def find_max_crossing_subarray(profits, low, middle, high):
    left_summa = float('-inf')
    summa = 0
    max_left = middle
    for i in range(middle, low - 1, -1):
        summa += profits[i][1]
        if summa > left_summa:
            left_summa = summa
            max_left = i

    right_summa = float('-inf')
    summa = 0
    max_right = middle + 1
    for j in range(middle + 1, high + 1):
        summa += profits[j][1]
        if summa > right_summa:
            right_summa = summa
            max_right = j
    return max_left, max_right, left_summa + right_summa


def find_maximum_subarray(profits, low, high):
    if high == low:
        return low, high, profits[low][1]
    else:
        middle = (low + high) // 2
        left_low, left_high, left_summa = find_maximum_subarray(profits, low, middle)
        right_low, right_high, right_summa = find_maximum_subarray(profits, middle + 1, high)
        cross_low, cross_high, cross_summa = find_max_crossing_subarray(profits, low, middle, high)

        if left_summa >= right_summa and left_summa >= cross_summa:
            return left_low, left_high, left_summa
        elif right_summa >= left_summa and right_summa >= cross_summa:
            return right_low, right_high, right_summa
        else:
            return cross_low, cross_high, cross_summa


def task6():
    data_read = read_from_file()
    data = [[elem.split(",")[2], float(elem.split(",")[4].strip())] for elem in data_read[1:]]
    for i in range(len(data) - 1):
        data[i] = [data[i][0], data[i + 1][1] - data[i][1]]
    buy_day, sell_day, max_profit = find_maximum_subarray(data, 0, len(data) - 1)
    write_in_file(f"Фирма: {data_read[1].split(',')[0]}\n"
                  f"Период: {data_read[1].split(',')[2]} - {data_read[-1].split(',')[2]}\n"
                  f"Дата покупки: {data[buy_day][0]}\n"
                  f"Дата продажи: {data[sell_day][0]}\n"
                  f"Сумма прибыли: {max_profit}")


if __name__ == "__main__":
    task6()
