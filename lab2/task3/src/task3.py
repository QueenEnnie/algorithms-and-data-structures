import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def merge_sort_count(numbers):
    if len(numbers) == 1:
        return numbers, 0

    middle = len(numbers) // 2
    left_half, left_inversions = merge_sort_count(numbers[:middle])
    right_half, right_inversions = merge_sort_count(numbers[middle:])
    merged, inversions = merge_and_count_inversions(left_half, right_half)
    return merged, (left_inversions + right_inversions + inversions)


def merge_and_count_inversions(left, right):
    new = [0 for _ in range(len(right) + len(left))]
    left_index, right_index, new_index = 0, 0, 0
    inversions = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            new[new_index] = left[left_index]
            left_index += 1
        else:
            new[new_index] = right[right_index]
            inversions += len(left) - left_index
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
    return new, inversions


def task3():
    print("Задание №3")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = str(merge_sort_count(data)[1])
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task3()
