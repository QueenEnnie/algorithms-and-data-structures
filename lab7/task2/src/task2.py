import os, sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab7.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def minimal_amount_of_operations(number):
    min_operations = [0] * (number + 1)
    path = [0] * (number + 1)

    for i in range(2, number + 1):
        min_operations[i] = min_operations[i - 1] + 1
        path[i] = i - 1
        if i % 2 == 0 and min_operations[i // 2] + 1 < min_operations[i]:
            min_operations[i] = min_operations[i // 2] + 1
            path[i] = i // 2
        if i % 3 == 0 and min_operations[i // 3] + 1 < min_operations[i]:
            min_operations[i] = min_operations[i // 3] + 1
            path[i] = i // 3
    result_path = []
    current = number
    while current != 0:
        result_path.append(current)
        current = path[current]
    result_path.reverse()

    return min_operations[number], result_path


def task2():
    print("Задание №2")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = minimal_amount_of_operations(int(read_from_file(PATH_INPUT)[0]))
    result = f"{result[0]}\n{' '.join(map(str, result[1]))}"
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task2()
