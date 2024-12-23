import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def longest_common_subsequence(first_sequence, second_sequence):
    lsc_table = [[0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)]
    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                lsc_table[i][j] = lsc_table[i - 1][j - 1] + 1
            else:
                lsc_table[i][j] = max(lsc_table[i - 1][j], lsc_table[i][j - 1])
    return lsc_table[len(first_sequence)][len(second_sequence)]


def task4():
    print("Задание №4")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    first_array = list(map(int, data[1].split()))
    second_array = list(map(int, data[3].split()))
    result = str(longest_common_subsequence(first_array, second_array))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task4()
