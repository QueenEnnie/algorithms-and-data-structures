import os, sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def is_fibonacci(number):
    first = 5 * number ** 2 + 4
    second = 5 * number ** 2 - 4
    return math.isqrt(first) ** 2 == first or math.isqrt(second) ** 2 == second


def check_numbers(array):
    result = []
    for elem in array:
        result.append("Yes" if is_fibonacci(elem) else "No")
    return result


def task6():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))
    array = list(map(int, read_from_file(PATH_INPUT)[1:]))
    result = "\n".join(check_numbers(array))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
