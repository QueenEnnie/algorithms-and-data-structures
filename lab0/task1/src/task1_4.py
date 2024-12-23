import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab0.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))

def new_addition(a, b):
    return a + b ** 2


def task1_4():
    print("Задание №1.4")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    a, b = map(int, read_from_file(PATH_INPUT)[0].split())
    result = str(new_addition(a, b))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1_4()
