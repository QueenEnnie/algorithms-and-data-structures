import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def binary_addition(first, second):
    first = list(map(int, first.zfill(max(len(first), len(second)))))
    second = list(map(int, second.zfill(max(len(first), len(second)))))
    new, save = [], 0
    for i in range(len(first) - 1, -1, -1):
        new += [(first[i] + second[i] + save) % 2]
        save = 1 if (first[i] + second[i] + save) // 2 > 0 else 0
    if save:
        new += [save]
    return new[::-1]

def task9():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    first_number, second_number = read_from_file(PATH_INPUT)[0].split()
    result = "".join(map(str, binary_addition(first_number, second_number)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task9()

