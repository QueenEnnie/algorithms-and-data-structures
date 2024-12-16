import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heapify_array(array, n, i, swaps):
    root = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and array[left_child] < array[root]:
        root = left_child
    if right_child < n and array[right_child] < array[root]:
        root = right_child
    if root != i:
        swap(array, i, root)
        swaps.append((i, root))
        heapify_array(array, n, root, swaps)


def build_heap(array):
    swaps = []
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify_array(array, len(array), i, swaps)
    return swaps

def task4():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    array = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    all_swaps = build_heap(array)
    result = "\n".join([str(len(all_swaps))] +
              [f"{elem[0]} {elem[1]}" for elem in all_swaps])
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task4()
