import os

from lab3.utils import read_from_file, write_in_file
from random import randint


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def three_way_partition(array, left_index, right_index):
    pivot = array[left_index]
    less_than, greater_than = left_index, right_index
    indicator = left_index

    while indicator <= greater_than:
        if array[indicator] < pivot:
            array[less_than], array[indicator] = array[indicator], array[less_than]
            less_than += 1
            indicator += 1
        elif array[indicator] > pivot:
            array[indicator], array[greater_than] = array[greater_than], array[indicator]
            greater_than -= 1
        else:
            indicator += 1
    return less_than, greater_than


def randomized_quick_sort(array, left_index, right_index):
    if left_index < right_index:
        index = randint(left_index, right_index)
        array[left_index], array[index] = array[index], array[left_index]
        less_than, greater_than = three_way_partition(array, left_index, right_index)
        randomized_quick_sort(array, left_index, less_than - 1)
        randomized_quick_sort(array, greater_than + 1, right_index)
    return array


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = " ".join(map(str, randomized_quick_sort(data, 0, len(data) - 1)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
