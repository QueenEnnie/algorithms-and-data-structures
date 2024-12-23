import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def longest_common_subsequence_three(first_sequence, second_sequence, third_sequence):
    n, m, l = len(first_sequence), len(second_sequence), len(third_sequence)
    lsc_table = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    lsc_table[i][j][k] = lsc_table[i - 1][j - 1][k - 1] + 1
                else:
                    lsc_table[i][j][k] = max(lsc_table[i - 1][j][k], lsc_table[i][j - 1][k], lsc_table[i][j][k - 1])
    return lsc_table[n][m][l]


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    first_array = list(map(int, data[1].split()))
    second_array = list(map(int, data[3].split()))
    third_array = list(map(int, data[5].split()))
    result = str(longest_common_subsequence_three(first_array, second_array, third_array))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
