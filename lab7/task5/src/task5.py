import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def longest_common_subsequence_three(first_sequence, second_sequence, third_sequence):
    common = set(first_sequence) & set(second_sequence) & set(third_sequence)
    if not common:
        return 0

    first_sequence = [value for value in first_sequence if value in common]
    second_sequence = [value for value in second_sequence if value in common]
    third_sequence = [value for value in third_sequence if value in common]

    m, l = len(second_sequence), len(third_sequence)
    previous = [[0] * (l + 1) for _ in range(m + 1)]

    for first_value in first_sequence:
        current = [[0] * (l + 1) for _ in range(m + 1)]
        for j in range(1, m + 1):
            second_value = second_sequence[j - 1]
            current_row = current[j]
            current_previous_row = current[j - 1]
            previous_row = previous[j]
            previous_previous_row = previous[j - 1]
            for k in range(1, l + 1):
                if first_value == second_value == third_sequence[k - 1]:
                    current_row[k] = previous_previous_row[k - 1] + 1
                else:
                    current_row[k] = max(previous_row[k], current_previous_row[k], current_row[k - 1])
        previous = current

    return previous[m][l]


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
