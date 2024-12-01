import os
from lab3.utils import read_from_file, write_in_file
from lab3.task1.src.task1 import randomized_quick_sort


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def find_h_index(array):
    randomized_quick_sort(array, 0, len(array) - 1)
    h_index = 0
    for index, number in enumerate(array[::-1]):
        if number >= index + 1:
            h_index = index + 1
        else:
            break
    return h_index


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[0].split(",")))
    result = str(find_h_index(data))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task5()
