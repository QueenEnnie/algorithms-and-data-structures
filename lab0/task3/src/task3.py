import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab0.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def fib_new(n):
    previous_last, last = 0, 1
    for _ in range(n):
        previous_last, last = last % 10, (last + previous_last) % 10
    return previous_last


def task3():
    print("Задание №3")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = str(fib_new(int(read_from_file(PATH_INPUT)[0])))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task3()
