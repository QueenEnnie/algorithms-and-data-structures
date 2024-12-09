import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))

def check_is_heap(array):
    n = len(array)
    for i in range(1, n // 2 + 1):
        if 2 * i <= n and array[i - 1] > array[2 * i - 1]:
            return False
        if 2 * i + 1 <= n and array[i - 1] > array[2 * i]:
            return False
    return True

def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    array = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = "YES" if check_is_heap(array) else "NO"
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
