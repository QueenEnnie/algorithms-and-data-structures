import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    middle = len(numbers) // 2
    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])
    return merge(left_half, right_half)


def merge(left, right):
    new = [0 for _ in range(len(right) + len(left))]
    left_index, right_index, new_index = 0, 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new[new_index] = left[left_index]
            left_index += 1
        else:
            new[new_index] = right[right_index]
            right_index += 1
        new_index += 1

    while left_index < len(left):
        new[new_index] = left[left_index]
        left_index += 1
        new_index += 1

    while right_index < len(right):
        new[new_index] = right[right_index]
        right_index += 1
        new_index += 1
    return new


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = " ".join(map(str, merge_sort(data)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task1()
